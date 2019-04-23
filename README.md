## Instalação

```bash
    python3 setup.py install
```

## Execução

```python
    from pmodel import Pmodel 
    # Classe pmodel
    modelo_ p = Pmodel(noValues=4, p=0.52, slope=-1.66, seed=0)
    
    # Geração da série temporal multifractal
    modelo_p.gen_pmodel()
```