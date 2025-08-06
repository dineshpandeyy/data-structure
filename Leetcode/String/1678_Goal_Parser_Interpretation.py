class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        return command.replace("()", "o").replace("(al)", "al")

class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        stack = []

        for i, char in enumerate(command):
            if char == "G":
                stack.append(char)
            elif char == "(":
                if command[i+1] == ")":
                    stack.append("o")
                else:
                    stack.append("al")
        return "".join(stack)

        