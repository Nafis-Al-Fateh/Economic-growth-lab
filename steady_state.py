def steady_state_k(s,alpha,delta,n,g):

    k_star = (s/(n+g+delta))**(1/(1-alpha))

    y_star = k_star**alpha

    return k_star,y_star
