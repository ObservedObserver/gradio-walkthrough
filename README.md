---
sdk: gradio
sdk_version: 3.50.2
app_file: app.py
pinned: false
---

# pygwalker-gradio
 
## App 1: Visual Exploration of AirBnB Listings in NYC using [pygwalker](https://github.com/Kanaries/pygwalker)
> [pygwalker]() is a Python library that turns your dataframe/data connection into an interactive visualization module that allows you to analysis the data with drag-and-drop/chat interface, like tableau/powerBI.

Play a live demo on hugging face spaces: [play pygwalker](https://huggingface.co/spaces/observedobserver/pygwalker-gradio)

Run the app

```bash
python app.py
```
<a href="https://huggingface.co/spaces/observedobserver/pygwalker-gradio">
<img width="1441" alt="pygwalker-dradio" src="https://github.com/ObservedObserver/gradio-walkthrough/assets/22167673/45a0cb53-360a-4dad-b0c9-e8583f938c99">
</a>

## Native Support for Gradio Integration
What is the native way to integrate pygwalker with gradio. pygwalker contains a feature called 'kernel computation', which runs a computation engine based on duckDB to handle the data queries from user's interaction.

This is a powerful feature but requires extra setup from pygwalker. Since `pygwalker>=0.3.10a2`, pygwalker provide a native support for gradio developers to enable this feature:

```python
import gradio as gr
import pandas as pd
from pygwalker.api.gradio import PYGWALKER_ROUTE, get_html_on_gradio
with gr.Blocks() as demo:
    df = pd.read_csv("xxx.csv")
    # use get_html_on_gradio, which contains the logic to enable kernel computation
    pyg_html = get_html_on_gradio(df, spec="gw.json", debug=True)
    gr.HTML(pyg_html)
app = demo.launch(app_kwargs={
    "routes": [PYGWALKER_ROUTE]
})
```