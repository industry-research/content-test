import streamlit as st

def check_number(input):
    try:
        # Convert it into integer
        val = int(input)
        return True
    except ValueError:
        try:
            # Convert it into float
            val = float(input)
            return True
        except ValueError:
            return False
        
@st.dialog(title="Save Results", width="small")
def save(result):
    st.write(f"The results have been saved!")
    # insert value saving here

production_values = {
    "All local production (100%)": 1.0, 
    "Most local production (75%)": 0.75, 
    "Some local production (50%)": 0.5, 
    "Little local production (25%)": 0.25, 
    "No local production (0%)": 0.0,
}

material_values = {
    "All local materials (100%)": 1.0, 
    "Most local materials (75%)": 0.75, 
    "Some local materials (50%)": 0.50, 
    "Little local materials (25%)": 0.25, 
    "No local materials (0%)": 0.0,
}
 
st.title("Local Content Calculator")

# creates a horizontal line
st.write("---")

# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

col1, col2 = st.columns(2)

result = {
    "company": "",
    "email": "",
    "good": "",
    "material": "",
    "production_level": "",
    "material_level": "",
    "production_weight": 0.0,
    "material_weight": 0.0,
    "overheads_margins_weight": 0.0,
    "local_content_value": 0.0,
}

with col1:
    # input company
    result["company"] = st.text_input(
        "Company Name",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        placeholder="ACME Corp.",
    )

    # input email
    result["email"] = st.text_input(
        "Email",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        placeholder="john@doe.com",
    )

    # input good
    result["manufactured_good"] = st.text_input(
        "Provide the name of your manufactured good",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        placeholder="Door, Window, Cable, Flooring, etc",
    )
    
    # input good
    result["material"] = st.text_input(
        "What material is the item made out of? Provide any other relevant details",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        placeholder="Timber, concrete..",
    )
    
    # input 1
    result["production_level"] = production_values[st.selectbox(
        "How much of the production is done within Australia and/or New Zealand? This includes research, design, manufacturing and/or construction.",
        (production_values.keys()),
    )]

    # input 2
    result["material_level"] = material_values[st.selectbox(
        "How much of the materials are sourced within Australia and/or New Zealand? This includes raw materials (e.g timber and metals), coatings (e.g solvents and paints) and electric components.",
        (material_values.keys()),
    )]

    # inputs 3
    st.caption("What portion of the total cost do materials, production and overheads & margins account for? “Overheads & margins” include costs or profits spent/generated within ANZ, including logistics (e.g storage and transport), sale mark-up and any costs not covered under production and material.")
    
    result["production_weight"] = st.text_input(
        "Production (percentage)",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        placeholder=str(33),
    )

    result["material_weight"] = st.text_input(
        "Material (percentage)",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        placeholder=str(33),
    )

    result["overheads_margins_weight"] = st.text_input(
        "Overheads and Margins (percentage)",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        placeholder=str(34),
    )

    # button magic
    if st.button("Compute", type="primary", use_container_width=True):
        if check_number(result["production_weight"]) and check_number(result["material_weight"]) and check_number(result["overheads_margins_weight"]):
            result["production_weight"] = float(result["production_weight"])/100.0
            result["material_weight"] = float(result["material_weight"])/100.0
            result["overheads_margins_weight"] = float(result["overheads_margins_weight"])/100.0
            if (result["production_weight"])+(result["material_weight"])+(result["overheads_margins_weight"]) != 1.0:
                col1.markdown('Please ensure that the percentages add up to a 100')
            else:
                result["local_content_value"] = float((result["production_weight"] * result["production_level"]) + (result["material_weight"] * result["material_level"]) + (result["overheads_margins_weight"] * 1))
                col2.markdown(f'# Final Percentage: {round(result["local_content_value"] * 100, 2)}%')
                with col2:
                    if st.button("Save", type="primary", use_container_width=True):
                        # check here if the email address is valid
                        save(result)

        else:
            col1.markdown('Please enter numbers for percentages')
