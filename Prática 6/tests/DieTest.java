import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;

public class DieTest {
	Die die;

	/**
	 * Construtor sem parâmetro.
	 */
	@Test
	public void testDie() {
		die = new Die();

	}

	/**
	 * Construtor com um inteiro.
	 */
	@Test
	public void testDieSide() {
		die = new Die(3);

	}

	/**
	 * Construtor com um inteiro invalido.
	 */
	@Test(expected = AssertionError.class)
	public void testDieSideInvalid() {
		new Die(1);

	}

	/**
	 * Construtor com dois inteiros.
	 */
	@Test
	public void testDieSideResult() {
		die = new Die(8, 1);

	}

	/**
	 * Construtor com o resultado maior que os lados.
	 */
	@Test(expected = AssertionError.class)
	public void testDieSideResultinvalid() {
		new Die(3, 4);
	}

	/**
	 * Construtor com lado invalido porém resultado válido.
	 */
	@Test(expected = AssertionError.class)
	public void testDieSideResultInvalid2() {
		new Die(1, 1);
	}

	/**
	 * Construtor com lado válido e resultado inválido.
	 */
	@Test(expected = AssertionError.class)
	public void testDieSideResultInvalid3() {
		new Die(3, 0);
	}

	/**
	 * Construtor com lado e resultado inválidos.
	 */
	@Test(expected = AssertionError.class)
	public void testSideResultInvalida4() {
		new Die(0, 0);
	}

	/**
	 * Inicializa um dado de 16 lados e resultado inicial 8 para todos os testes a
	 * seguir.
	 */
	@Before
	public void defaultDice() {
		die = new Die(16, 8);

	}

	/**
	 * Testa o método roll.
	 */
	@Test
	public void testRoll() {
		die.roll();

	}

	/**
	 * Testa o método getNumSides. Espera-se retornar 16 para o nosso dado.
	 */
	@Test
	public void testGetNumSides() {
		assertEquals(die.getNumSides(), 16);

	}

	/**
	 * Testa o método getResult. Espera-se retornar 8 para o nosso dado.
	 */
	@Test
	public void testGetResult() {
		assertEquals(die.getResult(), 8);

	}

	/**
	 * Testa o equals com parâmetro nulo.
	 */
	@Test
	public void testEqualsNull() {
		assertFalse(die.equals(null));

	}

	/**
	 * Testa o equals com parâmetro sendo o próprio objeto.
	 */
	@Test
	public void testEqualsSameObject() {
		assertTrue(die.equals(die));
	}

	/**
	 * Testa o equals com parâmetro sendo um objeto de outra classe (String).
	 */
	@Test
	public void testEqualsOtherType() {
		String string = "lulz";
		assertFalse(die.equals(string));
	}

	/**
	 * Testa o equals com parâmetro sendo um dado com mesma quantidade de lados e
	 * mesmo resultado.
	 */
	@Test
	public void testEqualsTrue() {
		Die die2 = new Die(16, 8);
		assertTrue(die.equals(die2));

	}

	/**
	 * Testa o equals com parâmetro sendo um dado de numeros de lados iguais mas com
	 * resultado diferente e vice-versa.
	 */
	@Test
	public void testEqualsFalse() {
		Die die2 = new Die(16, 5);
		assertFalse(die.equals(die2));
		Die die3 = new Die(10, 8);
		assertFalse(die.equals(die3));
	}

	/**
	 * Testa o método toString da classe.
	 */
	@Test
	public void testToString() {
		assertEquals("Num sides 16 result 8", die.toString());

	}

}
