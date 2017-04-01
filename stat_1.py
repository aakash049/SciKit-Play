
def calstat():
        import matplotlib

        matplotlib.use('Qt4Agg')
        from matplotlib import pyplot as plt
        vert = hori = 0
        with open('movefile.txt', 'r') as in_file:
            for line in in_file:
                if line[0] == '1':
                    vert += 1
                else:
                    hori += 1

        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        labels = 'Verical Moves', 'Horizontal Moves'
        sizes = [vert, hori]
        explode = (0, 0.1)

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie chart is drawn as a circle.
        plt.show()

