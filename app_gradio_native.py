import gradio as gr
import pandas as pd
from pygwalker.api.gradio import PYGWALKER_ROUTE, get_html_on_gradio
from datasets import load_dataset

with gr.Blocks() as demo:
    # load dataset
    dataset = load_dataset("gradio/NYC-Airbnb-Open-Data", split="train")
    df = dataset.to_pandas()
    pyg_app = get_html_on_gradio(df, spec="gw.json", debug=True)
    gr.HTML(pyg_app)

app = demo.launch(app_kwargs={
    "routes": [PYGWALKER_ROUTE]
})