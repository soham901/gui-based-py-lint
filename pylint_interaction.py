"""THIS SCRIPT WAS MADE TO SIMPLY INTRACT WITH PYLINT"""

#region Libraries
import os
#endregion

#region Variables

#endregion


def get_score(filepath):
    """This method will return the score by given filepath"""
    if filepath == '':
        return
    output_stream = os.popen('pylint ' + filepath)
    output = output_stream.read()
    for index in range(len(output.split())):
        if output.split()[index] == 'at':
            score_str = output.split()[index + 1].replace('/10', '')
            
            try:
                score = float(score_str)
            except ValueError:
                return 0.0
            return score


def get_output_lines(filepath) -> list:
    """This method will return the whole output in lines by given filepath"""
    if filepath == '':
        return
    output_stream = os.popen('pylint ' + filepath)
    output = output_stream.read().split('\n')
    # remove extra elements from output list
    output = output[1:-5]
    return output


def get_output_lines_count(filepath) -> int:
    """This method will return the count of output's lines"""
    return len(get_output_lines(filepath))


def get_output_warnings(filepath) -> list:
    """This method will return the output's in lines by given filepath"""
    result = []
    output_lines = get_output_lines(filepath)
    for line in output_lines:
        # Get the line number, column number, warning code, and warning message
        parts = line.split(':')
        ln = int(parts[1])
        cn = int(parts[2])
        wcode = parts[3].strip()
        wmsg = parts[4].strip()

        # Store the values in a dictionary and append it to the list
        winfo = {'ln': ln, 'cn': cn, 'wcode': wcode, 'wmsg': wmsg}
        result.append(winfo)

    return result






# pylint's warning:
# format = filename.py:linenum:colnum: warning_code: warning message (warning msg inshort)
# example = Test.py:6:0: C0103: Constant name "c" doesn't conform to UPPER_CASE naming style (invalid-name)
