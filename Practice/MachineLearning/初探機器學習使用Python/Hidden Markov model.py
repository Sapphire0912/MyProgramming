# 隱馬可夫模型
# (本書實在意義不明, 因此找其他的教學)
# (等之後再來學這個演算法, HMM與自然語言處理相關)
# 目前先了解書上理論的部分

import numpy as np
# 評估: 前向-後向演算法
class ForwardBackward:
    def __init__():
        self.observations = ['homepage', 'signup', 'product', 'checkout']
        self.states = ['Proospect', 'User', 'Customer']
        self.emissions = ['homepage', 'signup', 'product page', 'checkout', 'contact us']
    
        self.start_probability = {
            'Prospect': 0.8,
            'User': 0.15,
            'Customer': 0.05
        }

        self.transition_probability = np.array([
            [0.8, 0.15, 0.05],
            [0.05, 0.8, 0.15],
            [0.02, 0.95, 0.03]
        ])

        self.emission_probability = np.array([
            [0.4, 0.3, 0.3],  # homepage
            [0.1, 0.8, 0.1],  # signup
            [0.1, 0.3, 0.6],  # product
            [0.0, 0.1, 0.9],  # checkout
            [0.7, 0.1, 0.2]   # contact us
        ])

        self.end_state = 'Ending'

    def forward():
        forward = []
        f_previous = {}

        for i in xrange(1, len(self.observations)):
            f_curr = {}
            for state in self.states:
                if i == 0:
                    prev_f_sum = self.start_probability[state]
                else:
                    prev_f_sum = 0.0
                    for k in self.states:
                        prev_f_sum += f_previous.get(k, 0.0) * \
                            self.transition_probability[k][state]
                f_curr[state] = self.emission_probability[state][self.observations[i]]
                f_curr[state] = f_curr[state] * prev_f_sum
                forward.append(f_curr)
                f_previous = f_curr
                p_fwd = 0.0
                for k in self.states:
                    p_fwd += f_previous[k] * self.transition_probability[k][self.end_state]

                {'probability': p_fwd, 'sequence': forward}

    def backward():
        backward = []
        b_prev = {}

        for i in xrange(len(self.observations), 0, -1):
            b_curr = {}
            for state in self.states:
                if i == 0:
                    b_curr[state] = self.transition_probability[state][self.end_state]
                else:
                    total = 0.0
                    for k in self.states:
                        total += self.transition_probability[state][k] * \
                            self.emission_probability[k][self.observations[x_plus]] * \
                                b_prev[k]
            backward.insert(0, b_curr)
            b_prev = b_curr

        p_bkw = 0.0

        for s in self.states:
            total += self.start_probability[s] * \
                self.emission_probability[s][self.observations[0]] * \
                    b_prev[s]

        {'probability': p_bkw, 'sequence': backward}

    def forward_backword():
        size = len(self.observations)
        forward = forward()
        backward = backward()
        posterior = {}

        for s in self.states:
            posterior[s] = []
            for i in xrange(1, size):
                value = forward['sequence'][i][s] * \
                    backward['sequence'][i][s] / forward['probability']
            posterior[s].append()
        
        return [forward, backward, posterior]
            
