def getNumCor(data, response, threshold):
    """
    Takes a dataframe and response variable and returns the independent 
    variables that have a high correlation to the reponse variable. 

    Parameters
    ----------
    data : DataFrame
        DataFrame you'd like the numeric values extracted from
    response : str
        The response variable. Correlations with this variable will be 
        ordered from highest to lowest.
    threshold : int
        Independent variables must have a correlation coefficient above 
        this number to pass selection.

    Returns
    -------
    dataframe
        Returns a correlation matrix ordered by the highest correlation
        to the response variable.
    """
    numVar = data.select_dtypes(include=[np.number])

    correlations = numVar.corr()

    orderedCor = correlations[response].sort_values(ascending = False)

    topOrder = orderedCor[orderedCor > threshold]

    topNames = topOrder.index

    topCorVars = data[topNames]

    return topCorVars.corr()