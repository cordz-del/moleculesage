import streamlit as st
from rdkit import Chem
from rdkit.Chem import Draw
import pubchempy as pcp

# Function to get molecule from PubChem
def get_molecule(smiles):
    molecule = Chem.MolFromSmiles(smiles)
    return molecule

def get_pubchem_info(cid):
    compound = pcp.Compound.from_cid(cid)
    return compound

# Streamlit app
def main():
    st.title("Molecule Sage")
    st.write("Enter a SMILES string or PubChem CID to get molecule information.")

    smiles_input = st.text_input("SMILES string")
    cid_input = st.text_input("PubChem CID")

    if smiles_input:
        molecule = get_molecule(smiles_input)
        if molecule:
            st.write("Molecule Structure:")
            st.image(Draw.MolToImage(molecule))
        else:
            st.write("Invalid SMILES string.")

    if cid_input:
        try:
            cid = int(cid_input)
            compound = get_pubchem_info(cid)
            if compound:
                st.write("Compound Information:")
                st.write(f"Name: {compound.iupac_name}")
                st.write(f"Molecular Formula: {compound.molecular_formula}")
                st.write(f"Molecular Weight: {compound.molecular_weight}")
            else:
                st.write("No information found for this CID.")
        except ValueError:
            st.write("Invalid CID.")

if __name__ == "__main__":
    main()
