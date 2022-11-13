import re

def dot_bracket_align(mirna, mirna_dot_bracket):
    top_strand = re.sub("\).*$", "", mirna_dot_bracket)
    bottom_strand = re.sub("^.*\(\.*", "", mirna_dot_bracket)
    print(top_strand)
    print(bottom_strand)
    
    assert top_strand.count("(") == bottom_strand.count(")")

    top_list = [c for c, i in enumerate(top_strand) if i == "("] 

    bottom_strand_rev = bottom_strand[::-1]
    bottom_list = [c for c, i in enumerate(bottom_strand_rev) if i == ")"]

    assert len(top_list) == len(bottom_list)

    match = 0
    top_align = list()
    bottom_align = list()
    i = j = d = 0
    while len(top_strand) > 0 or len(bottom_strand_rev) > 0:
        try: 
            if top_strand[i] == "." and bottom_strand_rev[j] == ".":
                top_align.append("."); bottom_align.append(".")
                i += 1; j += 1; d += 1
                # top_strand[1:]; bottom_strand[1:]
                # top_strand.pop(0); bottom_strand.pop(0)
            elif top_strand[i] == "." and bottom_strand_rev[j] == ")":
                top_align.append("."); bottom_align.append("-")
                i += 1; j += 0; d += 1
                # top_strand[1:]
                # top_strand.pop(0)
            elif top_strand[i] == "(" and bottom_strand_rev[j] == ".":
                top_align.append("-"); bottom_align.append(".")
                i += 0; j += 1; d += 1
                # bottom_strand[1:]
                # bottom_strand.pop(0)
            elif top_strand[i] == "(" and bottom_strand_rev[j] == ")":
                top_align.append("("); bottom_align.append(")")
                i += 1; j += 1; d += 1
                # top_strand[1:]; bottom_strand[1:]
                # top_strand.pop(0); bottom_strand.pop(0)
        except IndexError:
            print(str(i) + "/" + str(len(top_strand)))
            # print("top:\t" + "".join(top_align)); print("bottom:\t" + "".join(bottom_align))
            while True:
                try:
                    top_align.append(top_strand[i])
                    i += 1
                    #print(len(top_strand))
                except IndexError:
                    break
            break
        
    consensus = "".join("|" if i == "(" else " " for i in top_align)
    print("top_align:\t" + "".join(top_align)); print("consensus:\t" + consensus); print("bottom_align:\t" + "".join(bottom_align))

    top_nt = list()
    j = 0
    for i in top_align:
        if i in (".", "("):
            top_nt.append(mirna[j])
            j += 1
        elif i == "-":
            top_nt.append("-")

    bottom_nt = list()
    j = 0
    for i in bottom_align:
        if i in (".", ")"):
            bottom_nt.append(mirna[::-1][j])
            j += 1
        elif i == "-":
            bottom_nt.append("-")
    # [bottom_nt.append(mirna[::-1][c]) if i in (".", "(") else bottom_nt.append("-") for c, i in enumerate(bottom_align) ]
    print("top_nt:\t\t" + "".join(top_nt)); print("consensus:\t" + consensus); print("bottom_nt:\t" + "".join(bottom_nt))

    top_nt_upper = [v.upper() if consensus[k] == "|" else v for k, v in enumerate(top_nt)]
    bottom_nt_upper = [v.upper() if consensus[k] == "|" else v for k, v in enumerate(bottom_nt)]

    print("top_nt_upper:\t\t" + "".join(top_nt_upper))
    print("consensus:\t\t" + consensus)
    print("bottom_nt_upper:\t" + "".join(bottom_nt_upper))


if __name__ == "__main__":
    mirna_seq = "gcugggcucucaaagugguugugaaaugcauuuccgcuuugcgcggcauaucacagccagcuuugaugagcuuagc"
    mirna_dot_bracket = "((((((((((((((((((((((((.((((.....(((.....))))))).))))))))).)))))).)))))))))"
    
    dot_bracket_align(mirna_seq, mirna_dot_bracket)


