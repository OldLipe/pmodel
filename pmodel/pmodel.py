############################################################################################
# Nome: Felipe Carvalho                                                                    #
# Disciplina: CAP-239                                                                      #
# Referência: http://www2.meteo.uni-bonn.de/staff/venema/themes/surrogates/pmodel/pmodel.m #
############################################################################################

import math as mt
import numpy as np
import statistics as st

class Pmodel:
        def __init__(self, noValues=256, p=0.375, slope=np.array([]), seed=0):
                """
                Construtor
                
                Atributos:
                        noValues: Tamanho da série que será gerada
                        p: Probabilidade associada a série gerada, na qual os valores proximo de 1 ou 0 atingem o pico
                        slope: Segundo Davis et al. caso a inclinação seja maior que -1 a série é estacionária, 
                        porém se a inclinação seja entre -1 e -3 é não-estacionária
                        seed: Semente para garantir a reprodutibilidade

                """
                self.noValues = noValues
                self.p = p
                self.slope = slope
                self.seed = seed        

        def gen_pmodel(self):
                """              
                pmodel
                
                Método de geração de séries temporais multifractais

                return série com arrendondamento em 5 dígitos 

                """
                noOrders = mt.ceil(mt.log2(self.noValues))
                noValuesGenerated = 2**(noOrders)
                
                y = 1
                for i in range(0, noOrders):
                        y = self._next_step_1d(y, self.p)

                if self.slope:
                        fourrierCoeff = self._fractal_spectrum_1d(self.noValues, self.slope / 2)
                        meanVal = np.mean(y)
                        stdy = st.stdev(y)
                        x = np.fft.ifft(y - meanVal, axis=0) # Cálculo dos coeficientes de Fourier da série temporal gerada pelo p-model
                        phase = np.angle(x) # Cálculo das fases, não são alteradas pelo filtro de Fourier
                        x = fourrierCoeff * np.exp(1j*phase) # Cálculo dos coeficientes complexos com uma determinada inclinação espectral, e com as fases do p-model
                        x = np.real(np.fft.fft(x, axis=0)) # Geração da integração fracionária da série temporal
                        x = x * stdy / st.stdev(x)
                        x = x + meanVal
                else:
                        x = y

                return np.round(x, decimals=5)

                
        def _next_step_1d(self, y, p):
                
                np.random.seed(self.seed)
                
                tam = np.size(y)
                y2 = np.zeros(tam*2)
                
                sign = np.random.rand(tam)-0.5
                sign = sign/np.abs(sign)
                
                y2[0:(2*tam)-1:2] = y + sign*(1-2*p)*y
                y2[1:(2*tam):2] = y - sign*(1-2*p)*y

                return y2


        def _fractal_spectrum_1d(self, noValues, slope):

                ori_vector_size = noValues
                ori_half_size = int(ori_vector_size / 2)
                a = np.zeros(ori_vector_size+1)
                
                valor = ori_half_size+2
                for t2 in range(1, valor):
                        index = t2-1
                        t4 = 2 + ori_vector_size - t2
        
                        if t4 > ori_vector_size:
                                t4 = t2
                        if index <= 0:
                                coeff = 0
                        else:
                                coeff = np.power(index, slope) 
                        a[t2] = coeff
                        a[t4] = coeff
                
                a[1] = 0
                
                return a[1:]

                

