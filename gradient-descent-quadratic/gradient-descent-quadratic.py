def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    
    out = x0
    for _ in range(steps):
        d = 2*a*out + b
        out -= d * lr

    return out