import pandas as pd
import plotly.graph_objects as go
import dash_mantine_components as dmc
from dash import Dash  # Импортируем Dash из dash
from dash_express import DashExpress, Page

# Получаем данные
get_df = lambda: pd.read_csv(r'C:UsersAsakuraDesktopDashudobreniya_salary_data.csv')  # Используем r'' для правильного указания пути

# Инициализируем приложение
app = DashExpress(logo='DashExpress')

# Создаем страницу дашборда
page = Page(
    app=app,                    # DashExpress app
    url_path='/',               # Путь страницы
    name='Overview',            # Название страницы
    get_df=get_df,              # Функция получения данных
)

# Функция построения графика
def bar_func(df):
    pv = pd.pivot_table(df, index='continent', values='lifeExp', aggfunc='mean').reset_index()  # Убедитесь, что используете правильные названия колонок
    fig = go.Figure([go.Bar(x=pv['continent'], y=pv['lifeExp'])])
    return fig

# Размечаем макет
page.layout = dmc.SimpleGrid(
    children=[
        page.add_graph(h='calc(100vh - 138px)', render_func=bar_func)
    ]
)

# По каким колонкам фильтруем
page.add_autofilter('continent', multi=True)
page.add_autofilter('country', multi=True)
page.add_autofilter('lifeExp', multi=True)

# Запуск приложения
if __name__ == '__main__':
    app.run_server(debug=True)  # Используем run_server для запуска приложения