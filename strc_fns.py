def rpm2mms(rpm, pitch):
    return [(rpm*pitch)/60]

def t2f(torque, pitch, eff):
    import math
    return [(torque*(2*math.pi*eff))/pitch]

def bslib_struc_fltr(balls,Fy):
    return [balls[balls.Ca>Fy].head()]

def motormax(motor_map):
    # Extract the maximum motor torque values for each motor speed

    motormax_list = [max(jmp) for jmp in zip(motor_map)]

def envelope(x_data, y_data):
    # calculate the envelope limits of data (duty cycle or motor map) to find edge conditions for system rating
    # adapted from https://stackoverflow.com/questions/34235530/python-how-to-get-high-and-low-envelope-of-a-signal

    from numpy import array, sign, zeros
    from scipy.interpolate import interp1d
    from matplotlib.pyplot import plot, show, grid

    s = y_data

    q_u = zeros(len(s))
    q_l = zeros(len(s))

    # Prepend the first value of (s) to the interpolating values. This forces the model to use the same starting
    # point for both the upper and lower envelope models.

    u_x = [0, ]
    u_y = [s[0], ]

    l_x = [0, ]
    l_y = [s[0], ]

    # Detect peaks and troughs and mark their location in u_x,u_y,l_x,l_y respectively.

    for k in range(1, len(s) - 1):
        if (sign(s[k] - s[k - 1]) == 1) and (sign(s[k] - s[k + 1]) == 1):
            u_x.append(k)
            u_y.append(s[k])

        if (sign(s[k] - s[k - 1]) == -1) and ((sign(s[k] - s[k + 1])) == -1):
            l_x.append(k)
            l_y.append(s[k])

    # Append the last value of (s) to the interpolating values. This forces the model to use the same ending point
    # for both the upper and lower envelope models.

    u_x.append(len(s) - 1)
    u_y.append(s[-1])

    l_x.append(len(s) - 1)
    l_y.append(s[-1])

    # Fit suitable models to the data. Here I am using cubic splines, similarly to the MATLAB example given in the
    # question.

    u_p = interp1d(u_x, u_y, kind='cubic', bounds_error=False, fill_value=0.0)
    l_p = interp1d(l_x, l_y, kind='cubic', bounds_error=False, fill_value=0.0)

    # Evaluate each model over the domain of (s)
    for k in range(0, len(s)):
        q_u[k] = u_p(k)
        q_l[k] = l_p(k)

    # Plot everything
    plot(x_data, s);
    #hold(True);
    plot(x_data, q_u, 'r');
    plot(x_data, q_l, 'g');
    grid(True);
    show()

    return q_u
