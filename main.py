def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    m_perc = int(input('Number of males:'))
    f_perc = int(input('Number of females:'))
    total = m_perc + f_perc 

    """
    You should make an expression to calculate the percentage
    m_perc  = m_perc / total * 100
    f_perc  = f_perc / total * 100
    """
    

    
    print(f"The total number of students: {total}")
    print(f"The number of males and females: {m_perc} {f_perc} ")
    print (f"The percentage of males and females: \t {m_perc:.2f}% {f_perc:.2f}%")

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc, total


if __name__ == '__main__':
    main()
