def project_estimate(ot, pt, mt):
    return (ot + pt + (4 * mt)) / 6

def main():
    while True:
        ot = input("Enter the number of hours for the optimistic time (or 'q' to quit): ")
        if ot.lower() == 'q':
            break
        pt = input("Enter the number of hours for the pessimistic time (or 'q' to quit): ")
        if pt.lower() == 'q':
            break
        mt = input("Enter the number of hours for the most likely time (or 'q' to quit): ")
        if mt.lower() == 'q':
            break
        
        try:
            ot = float(ot)
            pt = float(pt)
            mt = float(mt)
            print("The estimated time for the project is: ", project_estimate(ot, pt, mt))
        except ValueError:
            print("Please enter valid numbers for the times.")

if __name__ == "__main__":
    main()