def Anonimizza(nome,d,l):
    
  """ 
  La funzione riceve un nome e un dizionario in cui ad ogni nome utente è
  associato un codice identificativo. Se il nome non è presente nel dizionario,
  questo viene aggiunto con un nuovo codice (di lunghezza fissa l)
  
  Parameters
  ----------
  nome : str
      Nome utente da anonimizzare.
  d : dict
      Dizionario che associa ad ogni nome un codice identificativo.
  l : int
      Lunghezza del codice identificativo
  
  Returns
  -------
  d: dict
     Dizionario fornito in ingresso con eventuale aggiunta di "nome".
  
  """

  if nome not in d.keys():
      d[nome] = str(len(d)+1).zfill(l)
  return d



def Deanonimizza(codice,d):
    
    """
    La funzione riceve un codice identificativo e un dizionario, in cui ad ogni
    nome utente è associato un codice. Se il codice è presente nel dizionario, 
    la funzione restituisce il nome utente associato. Se il codice non è
    presente, non viene alterato.

    Parameters
    ----------
    codice : str
        Codice identificativo anonimo.
    d : dict
        Dizionario che associa ad ogni nome un codice identificativo.

    Returns
    -------
    nome : str
        Nome utente associato al codice identificativo.
    codice : str
        Codice identificativo anonimo.

    """
    
    trov = False
    for nome in d.keys():
        if d[nome] == codice:
            trov = True
            break
        
    if trov:
        return nome
    else:
        print('Al codice ', codice, ' non è associato nessun nome utente.')
        return codice
        