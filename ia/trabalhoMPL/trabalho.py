import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pyparsing import col
import seaborn as sns
import os
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split



#Função do cáculo da sigmóide
def sigmoid(x):
    return 1/(1+np.exp(-x))

caminhoPastaRaiz = os.getcwd()
dataSet = pd.read_csv(caminhoPastaRaiz + "/ia/trabalhoMPL/arruela_.csv")
dataSet.drop(["Hora", "Tamanho", "Referencia"], axis=1, inplace=True)

varInfo = [["NumAmostra", "Area", "Delta"]]
varDestino = [["Output1", "Output2"]]

scaler = StandardScaler()
dataScaled = scaler.fit_transform(dataSet)
dataSetScaled = pd.DataFrame(np.array(dataScaled), columns=["NumAmostra", "Area", "Delta", "Output1", "Output2"])
print(dataSetScaled.head())

varInfo = dataSetScaled.drop(["Output1", "Output2"], axis=1)
varDestino = dataSet[["Output1", "Output2"]]

varInfo_train, varInfo_test, varDestino_train, varDestino_test = train_test_split(varInfo, varDestino, test_size=0.30, random_state=101)

#Tamanho do DataSet de Treinamento
n_records, n_features = varInfo_test.shape
print(n_records)
print(n_features)

#Arquitetura da MPL
N_input = 3
N_hidden = 8
N_output = 2
learnrate = 0.1

#Pesos da Camada Oculta (Inicialização Aleatória)
pesos_camada_oculta = np.random.normal(0, scale=0.1, size=(N_input, N_hidden))

#Pesos da Camada de Saída (Inicialização Aleatória)
pesos_camada_saida = np.random.normal(0, scale=0.1, size=(N_hidden, N_output))

epochs = 200000
last_loss=None
EvolucaoError=[]
IndiceError=[]

for e in range(epochs):
    delta_p_c_o = np.zeros(pesos_camada_oculta.shape)
    delta_p_c_s = np.zeros(pesos_camada_saida.shape)
    for xi, yi in zip(varInfo_train.values, varDestino_train.values):
        #Camada oculta
        #Calcule a combinação linear de entradas e pesos sinápticos
        hidden_layer_input = np.dot(xi, pesos_camada_oculta)
        #Aplicado a função de ativação
        hidden_layer_output = sigmoid(hidden_layer_input)
    
        #Camada de Saída
        #Calcule a combinação linear de entradas e pesos sinápticos
        output_layer_in = np.dot(hidden_layer_output, pesos_camada_saida)

        #Aplicado a função de ativação 
        output = sigmoid(output_layer_in)
        #print('As saídas da rede são',output)
#-------------------------------------------    
    
# Backward Pass
        ## TODO: Cálculo do Erro
        error = yi - output
    
        # TODO: Calcule o termo de erro de saída (Gradiente da Camada de Saída)
        output_error_term = error * output * (1 - output)

        # TODO: Calcule a contribuição da camada oculta para o erro
        hidden_error = np.dot(pesos_camada_saida,output_error_term)
    
        # TODO: Calcule o termo de erro da camada oculta (Gradiente da Camada Oculta)
        hidden_error_term = hidden_error * hidden_layer_output * (1 - hidden_layer_output)
    
        # TODO: Calcule a variação do peso da camada de saída
        delta_p_c_s += output_error_term*hidden_layer_output[:, None]

        # TODO: Calcule a variação do peso da camada oculta
        delta_p_c_o += hidden_error_term * xi[:, None]
        
    #Atualização dos pesos na época em questão
    pesos_camada_oculta += learnrate * delta_p_c_o / n_records
    pesos_camada_saida += learnrate * delta_p_c_s / n_records
    
    
    # Imprimir o erro quadrático médio no conjunto de treinamento
    
    if  e % (epochs / 20) == 0:
        hidden_output = sigmoid(np.dot(xi, pesos_camada_oculta))
        out = sigmoid(np.dot(hidden_output,
                             pesos_camada_saida))
        loss = np.mean((out - yi) ** 2)

        if last_loss and last_loss < loss:
            print("Erro quadrático no treinamento: ", loss, " Atenção: O erro está aumentando")
        else:
            print("Erro quadrático no treinamento: ", loss)
        last_loss = loss
         
        EvolucaoError.append(loss)
        IndiceError.append(e)#Camada oculta
        #Calcule a combinação linear de entradas e pesos sinápticos
        hidden_layer_input = np.dot(xi, pesos_camada_oculta)
        #Aplicado a função de ativação
        hidden_layer_output = sigmoid(hidden_layer_input)
    
        #Camada de Saída
        #Calcule a combinação linear de entradas e pesos sinápticos
        output_layer_in = np.dot(hidden_layer_output, pesos_camada_saida)

        #Aplicado a função de ativação 
        output = sigmoid(output_layer_in)
        #print('As saídas da rede são',output)
#-------------------------------------------    
    
# Backward Pass
        ## TODO: Cálculo do Erro
        error = yi - output
    
        # TODO: Calcule o termo de erro de saída (Gradiente da Camada de Saída)
        output_error_term = error * output * (1 - output)

        # TODO: Calcule a contribuição da camada oculta para o erro
        hidden_error = np.dot(pesos_camada_saida,output_error_term)
    
        # TODO: Calcule o termo de erro da camada oculta (Gradiente da Camada Oculta)
        hidden_error_term = hidden_error * hidden_layer_output * (1 - hidden_layer_output)
    
        # TODO: Calcule a variação do peso da camada de saída
        delta_p_c_s += output_error_term*hidden_layer_output[:, None]

        # TODO: Calcule a variação do peso da camada oculta
        delta_p_c_o += hidden_error_term * xi[:, None]
        
    #Atualização dos pesos na época em questão
    pesos_camada_oculta += learnrate * delta_p_c_o / n_records
    pesos_camada_saida += learnrate * delta_p_c_s / n_records
    
    
    # Imprimir o erro quadrático médio no conjunto de treinamento
    
    if  e % (epochs / 20) == 0:
        hidden_output = sigmoid(np.dot(xi, pesos_camada_oculta))
        out = sigmoid(np.dot(hidden_output,
                             pesos_camada_saida))
        loss = np.mean((out - yi) ** 2)

        if last_loss and last_loss < loss:
            print("Erro quadrático no treinamento: ", loss, " Atenção: O erro está aumentando")
        else:
            print("Erro quadrático no treinamento: ", loss)
        last_loss = loss
         
        EvolucaoError.append(loss)
        IndiceError.append(e)


# Calcule a precisão dos dados de teste
n_records, n_features = X_test.shape
predictions=0

for xi, yi in zip(X_test.values, y_test.values):

# Forward Pass
        #Camada oculta
        #Calcule a combinação linear de entradas e pesos sinápticos
        hidden_layer_input = np.dot(xi, weights_input_hidden)
        #Aplicado a função de ativação
        hidden_layer_output = sigmoid(hidden_layer_input)
    
        #Camada de Saída
        #Calcule a combinação linear de entradas e pesos sinápticos
        output_layer_in = np.dot(hidden_layer_output, weights_hidden_output)

        #Aplicado a função de ativação 
        output = sigmoid(output_layer_in)

#-------------------------------------------    
    
#Cálculo do Erro da Predição
        ## TODO: Cálculo do Erro        
        if (output[0]>output[1]):
            if (yi[0]>yi[1]):
                predictions+=1
                
        if (output[1]>=output[0]):
            if (yi[1]>yi[0]):
                predictions+=1

print("A Acurácia da Predição é de: {:.3f}".format(predictions/n_records))