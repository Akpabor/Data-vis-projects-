{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\T\\anaconda3\\Lib\\site-packages\\pandas\\core\\arrays\\masked.py:60: UserWarning: Pandas requires version '1.3.6' or newer of 'bottleneck' (version '1.3.5' currently installed).\n",
      "  from pandas.core import (\n"
     ]
    }
   ],
   "source": [
    "import plotly.express as px\n",
    "import dash\n",
    "from dash import dcc\n",
    "from dash import html\n",
    "from dash.dependencies import Input, Output"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "\n",
       "        <iframe\n",
       "            width=\"100%\"\n",
       "            height=\"650\"\n",
       "            src=\"http://127.0.0.1:8050/\"\n",
       "            frameborder=\"0\"\n",
       "            allowfullscreen\n",
       "            \n",
       "        ></iframe>\n",
       "        "
      ],
      "text/plain": [
       "<IPython.lib.display.IFrame at 0x185904318d0>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "\n",
    "# Load Data\n",
    "df = px.data.tips()\n",
    "# Build App\n",
    "app = dash.Dash(__name__)\n",
    "app.layout = html.Div([\n",
    "    html.H1(\"Dash Demo\"),\n",
    "    dcc.Graph(id='graph'),\n",
    "    html.Label([\n",
    "        \"colorscale\",\n",
    "        dcc.Dropdown(\n",
    "            id='colorscale-dropdown', clearable=False,\n",
    "            value='plasma', options=[\n",
    "                {'label': c, 'value': c}\n",
    "                for c in px.colors.named_colorscales()\n",
    "            ])\n",
    "    ]),\n",
    "])\n",
    "# Define callback to update graph\n",
    "@app.callback(\n",
    "    Output('graph', 'figure'),\n",
    "    [Input(\"colorscale-dropdown\", \"value\")]\n",
    ")\n",
    "def update_figure(colorscale):\n",
    "    return px.scatter(\n",
    "        df, x=\"total_bill\", y=\"tip\", color=\"size\",\n",
    "        color_continuous_scale=colorscale,\n",
    "        render_mode=\"webgl\", title=\"Tips\"\n",
    "    )\n",
    "# Run app and display result inline in the notebook\n",
    "#app.run_server(mode='inline')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
