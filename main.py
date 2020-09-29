from Classes.courses_test import Course
import csv

from Classes.players import Player
raw_data = ['Status Total Players Pro Purse Last Updated Current Local Time\nEvent report received; official ratings pending. 59 $970 21-Sep-2020 07:34:34 CEST 25-Sep-2020 11:23:36 CEST', 'Place Name PDGA# Rating Par Rd1 Rd2 Total Prize (USD)\n1 Dennis Augustsson 98130 972 -18 52 1009 52 1005 104 $239\n2 Tobias Söderqvist 54111 986 -17 54 990 51 1014 105 $156\n3 Anders Pantzer 58188 950 -12 55 981 55 976 110 $117\n4 Rulle Eriksson 95621 986 -11 55 981 56 967 111\n5 Tomas Svahn 106139 985 -10 58 953 54 986 112 $63\n5 Max Regitnig 27812 990 -10 56 972 56 967 112 $63\n5 Rickard Sköld 57981 996 -10 54 990 58 948 112 $63\n8 Johan Amenda 59097 968 -9 59 943 54 986 113 $46\n8 Simon Clarenäs 64235 952 -9 55 981 58 948 113 $46\n10 Emil Blom 121599 931 -8 60 934 54 986 114 $40\n11 Melker Molin 81376 958 -7 60 934 55 976 115 $34\n12 Albin Widman 103830 960 -6 61 924 55 976 116\n12 Patrik Karlsson 55107 959 -6 57 962 59 938 116\n14 Thomas Svensson 50187 927 -5 61 924 56 967 117\n14 Karl Persson 115355 874 -5 59 943 58 948 117\n14 Jim Ljungqvist 140900 949 -5 59 943 58 948 117\n14 Pontus Snäll 46879 1003 -5 58 953 59 938 117\n18 Olle Samuelsson 35540 930 -2 64 896 56 967 120\n18 Henrik Karlberg 71408 940 -2 60 934 60 928 120\n18 David Johnsson 85229 893 -2 60 934 60 928 120\n21 Marcus Hallbjörner 96029 926 -1 63 906 58 948 121\n21 Simon Terbrant Säfström 101365 935 -1 62 915 59 938 121\n21 Henrik Rydén 53891 947 -1 60 934 61 919 121\n21 Sebastian Andersson 65147 909 -1 58 953 63 900 121\n25 Mikael Svensson 50186 936 E 64 896 58 948 122\n25 Benjamin Schiller 74340 958 E 62 915 60 928 122\n27 Jens Karlsson 74802 911 +2 67 868 57 957 124\n27 Jabbar Faraj 107764 875 +2 62 915 62 909 124\n27 Johannes Sandqvist 131751 +2 62 915 62 909 124\n30 Tommy Andersson 128023 902 +3 61 924 64 890 125\n30 Mikael Svensson 77547 909 +3 60 934 65 881 125\n32 Robin Tegerot 111060 894 +4 63 906 63 900 126\n33 Anton Wittgren 122763 899 +5 62 915 65 881 127\n33 Petter Ullman 121764 +5 60 934 67 862 127\n35 Marcus Bengtsson 107137 922 +6 67 868 61 919 128\n35 Anders Fagermoen 107931 853 +6 65 887 63 900 128\n37 Tommie Svensson 77535 891 +7 65 887 64 890 129\n38 Emil Hejde 81656 893 +8 63 906 67 862 130\n39 Kim Kestilä 112763 881 +9 70 840 61 919 131\n40 Carl Widlund 123975 849 +10 63 906 69 843 132\n41 Mikael Hejde 107525 884 +11 68 859 65 881 133\n42 Kenneth Edman 127682 854 +13 66 877 69 843 135\n43 Magnus Ekström 107285 875 +14 69 849 67 862 136\n44 Fredrik Björklund 124734 874 +15 67 868 70 833 137\n45 Anton Carlsson 127658 887 +16 67 868 71 824 138\n46 Mats Wahlqvist 105812 822 +20 71 830 71 824 142\n47 Leif Johansson +21 68 859 75 786 143\n48 Marc Hemgren 99121 +23 73 812 72 814 145\n49 Andreas Melin 49447 957 56 972 999 DNF\n49 Linus Harrysson 65 887 999 DNF', 'Place Name PDGA# Rating Par Rd1 Rd2 Total Prize (USD)\n1 Pia Andersson 111514 844 +8 66 877 64 890 130 $63\n2 Elin Clarenäs 64234 848 +18 70 840 70 833 140 $40\n3 Lisa Berlin 134935 776 +25 74 802 73 805 147\n4 Mimmi Granat 107746 718 +42 83 717 81 728 164\n5 Louise Bertilsson 123237 642 +45 86 689 81 728 167', 'Place Name PDGA# Rating Par Rd1 Rd2 Total\n1 Malte Svensson 92996 905 +3 62 915 63 900 125\n2 Albin Jacobsson 105240 881 +5 63 906 64 890 127\n2 Lukas Torstensson 114989 867 +5 62 915 65 881 127\n4 Gustav Askengren 132751 895 +17 64 896 75 786 139']


def main():
    ymergården = Course("YMERGÅRDEN", "BORÅS")
    ymergården.get_data("https://www.pdga.com/tour/event/46819")
    ymergården.plot_data()
    print(len(ymergården.latest_scores))

    # andreas = Player("Andreas", "Gustafsson")
    # for item in andreas.player_scores:
    #     print(f"{item}: {andreas.player_scores[item]}")


if __name__ == "__main__":
    main()
