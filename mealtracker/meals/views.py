# meals/views.py

from django.shortcuts import render, redirect
from .forms import MealForm
from .models import Meal
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# これは食事登録ページです、という簡単なテキストを返す
def add_meal_text(request):
    # クエリパラメーターの取得
    category = request.GET.get('category', '指定なし')  # 'category'パラメータがなければ'指定なし'をデフォルトにする
    date = request.GET.get('date', '指定なし')  # 'date'パラメータがなければ'指定なし'をデフォルトにする

    # クエリパラメーターを表示
    return HttpResponse(f"カテゴリ: {category}, 日付: {date}")

@login_required
def add_meal(request):
    # クエリパラメーターの取得
    category = request.GET.get('category', '指定なし')
    date = request.GET.get('date', '指定なし')

    # POSTリクエストが来た場合
    if request.method == 'POST':
        form = MealForm(request.POST, request.FILES)  # フォームにデータをセット
        if form.is_valid():  # フォームが有効なら
            meal = form.save(commit=False)  # フォームからデータを取得
            meal.user = request.user  # ユーザー情報を追加
            meal.save()  # 保存
            return redirect('meal_list')  # 食事一覧ページにリダイレクト
    else:
        form = MealForm()

    # クエリパラメーターをテンプレートに渡す
    return render(request, 'meals/add_meal.html', {'form': form, 'category': category, 'date': date})



