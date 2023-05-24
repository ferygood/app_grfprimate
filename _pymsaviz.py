#temporary pymsaviz function
from pymsaviz import MsaViz

msa_file = "static/ENSG00000288616_codon.fa"
mv = MsaViz(msa_file, wrap_length=100, show_consensus=True, show_count=True, consensus_color='#A3E4D7')

# Extract MSA positions less than 50% consensus identity
pos_ident_less_than_50 = []
ident_list = mv._get_consensus_identity_list()
for pos, ident in enumerate(ident_list, 1):
    if ident <= 50:
        pos_ident_less_than_50.append(pos)

# Add markers
mv.add_markers(pos_ident_less_than_50, marker="x", color="red")

mv.savefig("api_example03.png", dpi=200)