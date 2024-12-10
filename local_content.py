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
 
st.title("ICNVic - Local Content Calculator - External Version")

# creates a horizontal line
st.write("---")

# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

col1, col2 = st.columns(2)

with col1:
    # input 1
    production_level = production_values[st.selectbox(
        "What 'production' is local?",
        (production_values.keys()),
    )]

    # input 2
    material_level = material_values[st.selectbox(
        "What 'materials level' is local?",
        (material_values.keys()),
    )]

    # inputs 3
    st.caption("Ratios of item's cost:")
    
    production_weight = st.text_input(
        "Production (percentage)",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        placeholder=str(33),
    )

    material_weight = st.text_input(
        "Material (percentage)",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        placeholder=str(33),
    )

    overheads_margins_weight = st.text_input(
        "Overheads and Margins (percentage)",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        placeholder=str(34),
    )

    # button magic
    if st.button("Compute", type="primary", use_container_width=True):
        if check_number(production_weight) and check_number(material_weight) and check_number(overheads_margins_weight):
            production_weight = float(production_weight)/100.0
            material_weight = float(material_weight)/100.0
            overheads_margins_weight = float(overheads_margins_weight)/100.0
            if (production_weight)+(material_weight)+(overheads_margins_weight) != 1.0:
                col1.markdown('Please ensure that the percentages add up to a 100')
            else:
                local_content_value = float((production_weight * production_level) + (material_weight * material_level) + (overheads_margins_weight * 1))
                col2.markdown(f'# Final Percentage: {round(local_content_value * 100, 2)}%')
        else:
            col1.markdown('Please enter numbers for percentages')
