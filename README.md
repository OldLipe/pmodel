## Instalação

```bash
    python3 setup.py install
```

## Execução

```python
    from pmodel import pmodel as pm
    # Classe pmodel
    modelo_ p = pm.Pmodel(noValues=4, p=0.52, slope=-1.66, seed=0)
    
    # Geração da série temporal multifractal
    modelo_p.gen_pmodel()
```