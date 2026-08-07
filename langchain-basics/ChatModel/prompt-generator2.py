from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate(
    template="""
            Write a summary of book named "{book_input}" with the following specifications:
            Explanation Style: 
            ***
                Author Name
                Author Address
                Introduction
                Summary
                Conclusion
            ***
            Explanation Length: {length_input}
        """,
    input_variables=["book_input", "length_input"],
    validate_template=True
)

prompt.save('book-summary.json')