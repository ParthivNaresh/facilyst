import seaborn as sns

from facilyst.graph import Graph


class Scatter(Graph):

    name = "Scatterplot"

    def __init__(
        self, dataset=None, x=None, y=None, hue=None, style=None, plot_size=(11.7, 8.27)
    ):
        parameters = {"data": dataset, "x": x, "y": y, "hue": hue, "style": style}

        extra_parameters = {"plot_size": plot_size}

        sns_scatter = sns.scatterplot

        super().__init__(
            graph_obj=sns_scatter,
            parameters=parameters,
            extra_parameters=extra_parameters,
        )
