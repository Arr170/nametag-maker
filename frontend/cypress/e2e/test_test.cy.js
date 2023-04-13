describe('testing test', () => {
  it('tries to work', () => {
    cy.visit('https://nametags.onrender.com')

    cy.contains('small').click()

    cy.get('.inputs').type('fuckoff')
  })
})