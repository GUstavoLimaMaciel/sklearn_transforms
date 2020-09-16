from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        data.drop(labels=self.columns, axis='columns', inplace = True)        
        data.where(data["H_AULA_PRES"] > 0, inplace = True)
        data.dropna(axis='index', how='any', subset=['NOTA_DE', 'NOTA_EM', 'NOTA_MF', 'NOTA_GO','H_AULA_PRES'], inplace = True)

        return pd.get_dummies(data, columns=['REPROVACOES_DE', 'REPROVACOES_EM',
       'REPROVACOES_MF', 'REPROVACOES_GO','NOTA_DE', 'NOTA_EM', 'NOTA_MF', 'NOTA_GO', 'H_AULA_PRES'])
