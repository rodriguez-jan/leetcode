class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        def repeatString(substring):
            # repeat the string based on the positive integer attached to it
            # repeat anything from the start of integer and open bracket"
            # return the String to repeat
            # When nested loop, call in repeat string again
            # Terminate upon first close bracket call
            total_string = ""
            string_to_repeat = ""
            for i, temp2 in enumerate(substring):
                if temp2 == "]":
                    break
                if temp2.isdigit():
                    string_to_repeat += (repeatString(substring[i + 1::]))
                if (not temp2.isdigit()) and (temp2 != "["):
                    string_to_repeat += (temp2)
            return string_to_repeat

        total_string = ""
        nested = 0
        # Iterate through entire string
        for i, temp in enumerate(s):
            # Check for integers
            if temp.isdigit() and nested == 0:
                temp_length = temp
                if (temp_length == temp):
                    test = repeatString(s[i + 1::])
                for repeats in range(int(temp_length)):
                    total_string += (test)
                continue
            if temp == "[":
                nested += 1
            if nested == 0 and temp != "]" and not temp.isdigit() and temp != "[":
                total_string += temp
            if temp == "]":
                nested -= 1

        return total_string
        # Call repeatString when neccessary
        # Append all multiplied values to a total string







