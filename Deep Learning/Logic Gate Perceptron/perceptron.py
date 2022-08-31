import numpy as np


class Perceptron():
    def __init__(self, input, bias=1.0):  # input is a list of inputs, bias is by default 1
        """
        The length of input list is the (total number of inputs + 1)
        1 is added to the length considering the bias value
        The weights would be used in general
        :param input: The list of inputs provided to the perceptron
        :param bias: The bias is provided as 1.0 in general
        """
        self.weight = (np.random.rand(input + 1) * 2) - 1  # weights are random numbers
        self.bias = bias

    def sigmoid(self, x):
        # The activation function is sigmoid function (limiting outputs between 0 and 1, as needed by the output of Logic Gates
        return 1 / (1 + np.exp(-x))  # Formula for sigmoid function

    def run(self, value):
        # value contains the list of input values
        sum = np.dot(np.append(value, self.bias), self.weight)
        """
        We will calculate the dot product of the input values and the weights
        The bias value has been appended to the input values as it would be the final input after each iteration
        """
        return self.sigmoid(sum)

    def weight_array(self, weight_arr):
        # Returns the array of weights based on the weight input
        self.weight = weight_arr


# This function will be called from inside the main function when the values and bias are needed to be passed into the perceptron
# The "input_array" is the list containing input values followed by the bias
def get_result(input_array):
    perceptron = Perceptron(2)  # The perceptron is created with 2 inputs (for a logic gate)
    perceptron.weight_array(input_array)
    """
    The input values must be set as such that, 
    the sum produced by the dot product of the input values and the weights 
    is negative for a result of 0 and a positive value for a result of 1
    The values when passed to the sigmoid function will set the outputs.
    For a negative value the output will be close to 0 and 
    for a positive value, output is close to 1
    """

    print("-" * 20)
    print("| A | B |  Output  |")
    print("-" * 20)
    print("| 0 | 0 |  {0:.5f} |".format(
        perceptron.run([0, 0])))  # Limit O/P to 5 decimal places to reduce terminal spam
    print("| 0 | 1 |  {0:.5f} |".format(perceptron.run([0, 1])))
    print("| 1 | 0 |  {0:.5f} |".format(perceptron.run([1, 0])))
    print("| 1 | 1 |  {0:.5f} |".format(perceptron.run([1, 1])))

    print("""
    The output we see has values very close to 0 and 1
    We can round them off to 0 and 1 respectively
    """)


# Driver code
if __name__ == '__main__':
    print("Choose the logic gate:\nAND gate[A]\nOR gate[B]\n")
    gate = input("Your choice: ").upper()
    match gate:
        case "A":
            """
            The inputs provided, gives an output that satisfies the condition for AND gate
            inputs = 10, 10 and bias = (-15)
            The inputs and the bias has been passed into the function as a list
            """
            print("AND gate:")
            get_result([10, 10, -15])
        case "B":
            """
            The inputs provided, gives an output that satisfies the condition for AND gate
            inputs = 15, 15, bias = (-10)
            The inputs and the bias has been passed into the function as a list
            """
            print("OR gate:")
            get_result([15, 15, -10])

