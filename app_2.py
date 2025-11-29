import dash 
from dash import html
from dash.dependencies import Input, Output, ALL, MATCH
import feffery_antd_components as fac
from feffery_dash_utils.style_utils import style 

app = dash.Dash(__name__)



app.layout = html.Div(
    fac.AntdSpace(
        [
            fac.AntdSpace(
                [
                    fac.AntdTooltip(
                        fac.AntdButton(
                            f"按钮{i}",
                            id = {"type":"botton", "index":i},
                            type="primary"
                        ),
                        id={"type":"tooltip", "index":i}
                    )
                    for i in range(10)
                ],
                wrap=True
            )
        ],
        direction="vertical",
        style=style(width="100%")
    ),
    style=style(padding=50)
)

# 这里使用的是ALL的解决办法
@app.callback(
    Output({"type":"botton", "index":ALL}, "danger"),
    Input({"type":"botton", "index":ALL}, "nClicks"),
    prevent_initial_call=True
)
def update_bottons(nClicksList):
    return [bool(nClicks) for nClicks in nClicksList]


if __name__ == "__main__":
    app.run(debug=True)