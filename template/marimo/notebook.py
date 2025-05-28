import marimo

__generated_with = "0.13.11-dev14"
app = marimo.App(layout_file="layouts/notebook.slides.json")


@app.cell(hide_code=True)
def _(leaves, mo):
    mo.md(
        f"""
        # marimo slides! {"🍃" * leaves.value}

        **A presentation by the marimo team.**

        {leaves}
        """
    ).left().center()
    return


@app.cell
def _(mo):
    leaves = mo.ui.slider(1, 12)
    return (leaves,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **marimo** is an open-source Python notebook that's reproducible, shareable as an app, and executable as a script.

    Install it with `pip install marimo`, and learn more at [GitHub](https://github.com/marimo-team/marimo).

    Starting with **v0.7.2**, every marimo notebook can be shared as an interactive slide deck.

    **In fact, this slide deck was made with a marimo notebook!** To present your notebook as slides, just toggle the app view and choose the slide layout in the top right. Every cell with an output becomes its own slide.

    Next are a couple of examples of dynamic slides.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"## Dynamic plots").center()
    return


@app.cell
def _(mo):
    exponent = mo.ui.slider(1, 3, label="exponent")
    return (exponent,)


@app.cell
def _(exponent, mo, np):
    x = np.linspace(-3, 3, 100)
    y = x**exponent.value

    mo.md(
        rf"""
        {exponent}

        \[
        y = x^{exponent.value}
        \]

        {mo.as_html(make_plot(x, y))}
        """
    ).center()
    return


@app.function
def make_plot(x, y):
    import matplotlib.pyplot as plt

    plt.plot(x, y)
    plt.ylim(-27, 27)
    plt.xlim(-3, 3)
    return plt.gca()


@app.cell
async def _():
    df = await make_data()
    return (df,)


@app.cell
def _(mo):
    mo.md("""# Select data in plots""")
    return


@app.cell
def _(df, mo):
    import altair as alt

    chart = mo.ui.altair_chart(
        alt.Chart(df)
        .mark_circle(size=60)
        .encode(
            x="Horsepower",
            y="Miles_per_Gallon",
            color="Origin",
            tooltip=["Name", "Origin", "Horsepower", "Miles_per_Gallon"],
        )
    )
    return (chart,)


@app.cell
def _(chart, mo):
    mo.vstack([mo.md("**Click and drag to select data.**"), chart, chart.value])
    return


@app.function
async def make_data():
    try:
        import micropip

        await micropip.install("vega_datasets")
    finally:
        ...

    from vega_datasets import data

    return data.cars()


@app.cell
def _(mo):
    mo.md(r"""## Thanks!""")
    return


@app.cell
def _():
    import numpy as np

    return (np,)


@app.cell
def _():
    import marimo as mo

    return (mo,)


if __name__ == "__main__":
    app.run()
