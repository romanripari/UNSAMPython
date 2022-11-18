# %%
import pandas as pd
def grafica_marea(filename, desde, hasta, delta_t, delta_h):
    df = pd.read_csv(filename, index_col=['Time'], parse_dates=True)
    if hasta == '':
        dh = df[desde:].copy()
    elif desde == '':
        dh = df[:hasta].copy()
    else:
        dh = df[desde:hasta].copy()
    pd.DataFrame([dh['H_SF'].shift(delta_t) - delta_h, dh['H_BA']]).T.plot()

def run():
    filename = '../Data/OBS_SHN_SF-BA.csv'
    delta_t = -1 # tiempo que tarda la marea entre ambos puertos
    delta_h = 13 # diferencia de los ceros de escala entre ambos puertos
    desde = '12-25-2014'    # Formato mm-dd-yyyy
    hasta = '12-27-2014'              # Formato mm-dd-yyyy
    grafica_marea(filename, desde, hasta, delta_t, delta_h)

if __name__ == '__main__':
    run()