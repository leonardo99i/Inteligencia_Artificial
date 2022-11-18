import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


if __name__=="__main__":

  #variáveis de entrada:
  velocidade = ctrl.Antecedent(np.arange(0, 101, 1), 'velocidade')
  potencia = ctrl.Antecedent(np.arange(0, 151, 1), 'potencia')

  #variável de saída:
  tempo = ctrl.Consequent(np.arange(0, 13, 1), 'risco')

  #fuzzificação:
  velocidade['minima'] = fuzz.trimf(velocidade.universe, [0, 25, 50])
  velocidade['medio'] = fuzz.trimf(velocidade.universe, [25, 50, 75])
  velocidade['maxima'] = fuzz.trimf(velocidade.universe, [50, 75, 100])

  potencia['motor_1.6'] = fuzz.trapmf(potencia.universe, [0, 0, 50, 100])
  potencia['motor_1.8'] = fuzz.trimf(potencia.universe, [50, 85, 120])
  potencia['motor_2.0'] = fuzz.trapmf(potencia.universe, [80, 120, 150, 150])
  
  #definindo as regras
  regra1 =ctrl.Rule(potencia['1.6'] | velocidade[])
  regra2 = 
  regra3 =
  
  #ativação de regras
  tempo_de_chegada = ctrl.ControlSystem([regra1, regra2, regra3])
  potencia_motor = ctrl.ControlSystemSimulation(tempo_de_chegada)
  

  potencia.view()