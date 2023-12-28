#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def get_roots(number_of_samples_to_add: int, one_root: bool, two_roots:bool, no_roots: bool) -> pd.DataFrame: 
    start_range = -100
    end_range = 100
    start_range_coeff = 1
    end_range_coeff = 10
    coeffs = []
    range_coeff = [i for i in range(start_range, end_range + 1) if i != 0]
    multiply_coeff = [i for i in range(start_range_coeff, end_range_coeff + 1)]
    a = np.random.choice(range_coeff, number_of_samples_to_add)
    b = np.random.choice(range_coeff, number_of_samples_to_add)
    intercepts = np.random.choice(range_coeff, number_of_samples_to_add)
    coeff = np.random.choice(multiply_coeff, number_of_samples_to_add)
    if number_of_samples_to_add >= 0:
        for root_1, root_2, intercept, ksi in zip(a, b, intercepts, coeff):
            if root_1 == root_2:
                if one_root:
                    alpha = ksi 
                    beta = -2*ksi*root_1
                    gamma = ksi*root_1*root_1
                    coeffs.append(get_source(alpha, beta, gamma, no_roots=False))
            elif root_1 != root_2 and root_1 != (-1)*root_2:
                if one_root:
                    alpha = ksi
                    beta = -ksi*(root_1 + root_2)
                    gamma = ksi*root_1*root_2
                    coeffs.append(get_source(alpha, beta, gamma, no_roots=False))
                if no_roots:
                    D = root_2*root_2 - 4*root_1*intercept
                    if D < 0:
                        coeffs.append(get_source(root_1, root_2, intercept, no_roots=True))
                    else:
                        continue
    dataset_roots = pd.DataFrame(coeffs, columns=['text'])
    return dataset_roots


def get_source(alpha: int, beta: int, gamma: int, no_roots: bool) -> list:
    if beta > 0 and alpha > 0 and gamma > 0:
        source = f"{alpha}x^2+{beta}x+{gamma}=0"
    elif beta > 0 and alpha < 0 and gamma > 0:
         source = f"{alpha}x^2+{beta}x+{gamma}=0"
    elif beta > 0 and alpha < 0 and gamma < 0:
        source = f"{alpha}x^2+{beta}x{gamma}=0"   
    elif beta > 0 and alpha > 0 and gamma < 0:
         source = f"{alpha}x^2+{beta}x{gamma}=0" 
    elif beta < 0 and alpha > 0 and gamma > 0:
        source = f"{alpha}x^2{beta}x+{gamma}=0"
    elif beta < 0 and alpha < 0 and gamma > 0:
        source = f"{alpha}x^2{beta}x+{gamma}=0"
    elif beta < 0 and alpha > 0 and gamma < 0:
        source = f"{alpha}x^2{beta}x{gamma}=0"
    else:
        source = f"{alpha}x^2{beta}x{gamma}=0"

    D = beta*beta - 4*alpha*gamma

    if alpha == beta:
        if beta > 0:
            solution = f"D=({beta}^2-4*{alpha}*{gamma})={D};x=(-{beta}/(2*({alpha}))={-beta/(2*alpha)};x=(-{beta}/(2*({alpha}))={-beta/(2*alpha)}"
            answer = f"x={-beta/(2*alpha)};"
            equation = f"{source};{solution};{answer}"
        elif beta < 0:
            solution = f"D=({beta}^2-4*{alpha}*{gamma};x=({(-1)*beta}/(2*({alpha}))={-beta/(2*alpha)};x=({(-1)*beta}/(2*({alpha}))={-beta/(2*alpha)}"
            answer = f"x={-beta/(2*alpha)};"
            equation = f"{source};{solution};{answer}"
    elif alpha != beta:
        if beta > 0:
            solution = f"D=({beta}^2-4*{alpha}*{gamma})={D};x=(-{beta}-{np.sqrt(D)})/(2*{alpha})={(-beta-np.sqrt(D))/(2*alpha)}; x=(-{beta}+{np.sqrt(D)})/(2*{alpha})={(-beta+np.sqrt(D))/(2*alpha)}"
            answer = f"x={(-beta-np.sqrt(D))/(2*alpha)};x={(-beta+np.sqrt(D))/(2*alpha)};"
            equation = f"{source};{solution};{answer}"
        elif beta < 0:
            solution = f"D=({beta}^2-4*{alpha}*{gamma})={D};x=({(-1)*beta}-{np.sqrt(D)})/(2*{alpha})={(-beta-np.sqrt(D))/(2*alpha)}; x=({beta}+{np.sqrt(D)})/(2*{alpha})={(-beta+np.sqrt(D))/(2*alpha)}"
            answer = f"x={(-beta-np.sqrt(D))/(2*alpha)};x={(-beta+np.sqrt(D))/(2*alpha)};"
            equation = f"{source};{solution};{answer}"
    if no_roots:
        source = f"{alpha}x^2+{beta}x+{gamma}=0"
        solution = f"D=({beta}^2-4*{alpha}*{gamma})={beta*beta - 4*alpha*gamma}"
        answer = f"x=no roots;"
        equation = f"{source};{solution};{answer}"

    return equation

