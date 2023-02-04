import pandas as pd
def describe_df(func):
    def wrapper():
        func()
        print(f'El tamano del data set es: {func().shape}')
        print(f'Los tipos de datos del dataset son:\n{func().dtypes}')

    return wrapper


@describe_df
def data_csv():
    df = pd.read_csv('data.csv')
    return df
def run():
    data_csv()

if __name__ == '__main__':
    run()