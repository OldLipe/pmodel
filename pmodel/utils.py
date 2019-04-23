def desvio_padrao(y):
        """
        
        Cálculo de desvio-padrão amostral
        
        """
        n = len(y) - 1
        dp = mt.sqrt(sum((y - np.mean(y)) * (y - np.mean(y)))/n)
        return dp


 

