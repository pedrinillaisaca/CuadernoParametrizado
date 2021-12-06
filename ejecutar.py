import papermill as pm
pm.execute_notebook(
 'Prueba1_param.ipynb',
 'Prueba1_param_out.ipynb',
 parameters=dict(rango1='2017',rango2='2022'),
 kernel_name='python3'
)