def Predict(X_user) :
    # Libs
    import pandas as pd
    import numpy as np

    X_user = np.array(X_user).reshape(1,-1)
    print(X_user)
    # Reading the dataset
    dataset = pd.read_csv("dataset(class-reg).csv")

    X_class = dataset.iloc[:,:-2].values
    X_reg = dataset.iloc[:,:-2].values
    Y_class = dataset.iloc[:,-2].values
    Y_reg = dataset.iloc[:,-1].values

    X_class = np.concatenate((X_class, X_user))
    X_reg = np.concatenate((X_reg, X_user))

    print('Regression - 1')
    # Regression-1 :
    X_reg1 = X_reg
    Y_reg1 = Y_reg

    # Categorical Variables
    from sklearn.preprocessing import LabelEncoder
    lb = LabelEncoder()
    X_reg1[:,0] = lb.fit_transform(X_reg1[:,0])
    X_reg1[:,4] = lb.fit_transform(X_reg1[:,4])
    X_reg1[:,7] = lb.fit_transform(X_reg1[:,7])
    X_reg1[:,9] = lb.fit_transform(X_reg1[:,9])
    X_reg1[:,10] = lb.fit_transform(X_reg1[:,10])

    X_reg1 = X_reg1.astype(np.float64)

    # Scaler
    from sklearn.preprocessing import StandardScaler
    sc_X1 = StandardScaler()
    sc_Y1 = StandardScaler()
    X_reg1 = sc_X1.fit_transform(X_reg1)
    Y_reg1 = sc_Y1.fit_transform(Y_reg1.reshape(-1,1))

    # Train and Test
    X_reg1_train = X_reg1[:-1,:]
    X_reg1_test = X_reg1[-1:,:]
    Y_reg1_train = Y_reg1


    #Random Forest
    from sklearn.ensemble import RandomForestRegressor
    regressor1 = RandomForestRegressor(n_estimators = 1500)
    regressor1.fit(X_reg1_train, Y_reg1_train)

    pred1 = regressor1.predict(X_reg1_test)

    pred1 = sc_Y1.inverse_transform(pred1)
            
    #--------
    print('Regression - 2')
    # Regression-2 :
    X_reg2 = X_reg
    Y_reg2 = Y_reg
    # Categorical Variables
    from sklearn.preprocessing import OneHotEncoder
    from sklearn.compose import make_column_transformer
    column = make_column_transformer((OneHotEncoder(drop = "first", sparse = False), [0,4,7,9,10]),
                                             remainder = "passthrough")
    X_reg2 = column.fit_transform(X_reg2)

    # Scaler
    from sklearn.preprocessing import StandardScaler
    sc_X2 = StandardScaler()
    sc_Y2 = StandardScaler()
    X_reg2 = sc_X2.fit_transform(X_reg2)
    Y_reg2 = sc_Y2.fit_transform(Y_reg2.reshape(-1,1))

    # Train and Test
    X_reg2_train = X_reg2[:-1,:]
    X_reg2_test = X_reg2[-1:,:]
    Y_reg2_train = Y_reg2


    #CatBoost
    from catboost import CatBoostRegressor
    regressor2 = CatBoostRegressor(learning_rate = 0.125, iterations = 950)
    regressor2.fit(X_reg2_train, Y_reg2_train)

    pred2 = regressor2.predict(X_reg2_test)

    pred2 = sc_Y2.inverse_transform(pred2)

    #Combining :
    pred_reg = pred1 * 0.5 + pred2 * 0.5

    return pred_reg            
