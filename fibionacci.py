while True:
    try:
        number_of_terms = int(input("Number of Terms: "))
        terms = [0,1]
        term_str = "1"
        for i in range(number_of_terms):
            next_term = terms[-1]+terms[-2]
            terms.append(next_term)
            term_str += ", "+str(next_term)
        terms = terms[1:]
        print(term_str)
    except ValueError:
        print('Please enter a valid integer')
        continue
    except KeyboardInterrupt:
        break