#stochastic gradient decent
#using theano as T

params  = [weights_hidden, weights_op, bias_hidden, bias_op]

def sgd(cost, params, lr = 0.05):
    grads = T.grad(cost=cost, wrt=params)
    updates = []

    for p,g in zip(params,grads):
        updates.append([p,p-g*lr])

    return updates

updates = sgd(cost,params)
