# CGR-analysis-tool

![gopher](https://cdn.dribbble.com/userupload/2624050/file/original-59266f4dea1c2aa43f2064cc0f3b165a.png?resize=400x0)

### Installation 
Download git bash (64-bit version):
https://git-scm.com/download/win

- open git bash
- clone this repository:  ```git clone <url>```

### Download dependencies:
```shell
cd CGR-analysis-tool
pip install poetry
poetry install
```

### Run
Run .py file:
```shell
poetry run python scripts/example_py.py 
```
Run jupyter file:
Simply run as usual

### Lint
```shell
poetry run task lint
```

### Test
```shell
poetry run task test
```

### Ressources

[plotly documentation](https://plotly.com/python/)

[dash documentation](https://dash.plotly.com/)

[dash course](https://www.youtube.com/watch?v=RMBSQ6leonU&ab_channel=CharmingData)

[map tool](https://kepler.gl/)

[pandas-profiling](https://github.com/ydataai/pandas-profiling)