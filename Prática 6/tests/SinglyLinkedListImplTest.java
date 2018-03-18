import org.junit.Before;
import org.junit.Test;

public class SinglyLinkedListImplTest {
	SinglyLinkedListImpl<Integer> list;

	/**
	 * Inicializa uma lista.
	 */
	@Before
	public void init() {
		list = new SinglyLinkedListImpl<>();
	}

	/**
	 * Testa o método add, adicionando numa lista vazia e depois numa lista com um
	 * elemento.
	 */
	@Test
	public void addTest() {
		list.add(1);
		list.add(2);
	}

	/**
	 * Testa o addAfter colocando um elemento no meio.
	 */
	@Test
	public void addAfterTest() {
		list.add(1);
		list.add(3);
		list.addAfter(2, 1);
	}

	/**
	 * Adiciona depois do ultimo elemento da lista.
	 */
	@Test
	public void addAfterLastTest() {
		list.add(1);
		list.add(2);
		list.addAfter(3, 2);
	}

	/**
	 * Adiciona depois com um elemento inválido(Não está na lista).
	 */
	@Test
	public void addAfterNonExistentTest() {
		list.addAfter(2, 1);
	}

	/**
	 * DeleteFront com uma lista de apenas um elemento.
	 */
	@Test
	public void deleteFrontSingleElementTest() {
		list.add(1);
		list.deleteFront();
	}

	/**
	 * DeleteFront com uma lista de dois elementos, espera-se deletar o elemento 1.
	 */
	@Test
	public void deleteFrontTwoElementsTest() {
		list.add(1);
		list.add(2);
		list.deleteFront();
	}

	/**
	 * Tenta deletar a cabeça de uma lista vazia. Espera-se exceção.
	 */
	@Test(expected = NullPointerException.class)
	public void deleteFrontNoElementTest() {
		list.deleteFront();
	}

	/**
	 * Tenta deletar depois de um elemento unico da lista. Espera-se exceção.
	 */
	@Test(expected = NullPointerException.class)
	public void deleteAfterLastElementTest() {
		list.add(1);
		list.deleteAfter(1);
	}

	/**
	 * Tenta deletar depois de dois elementos da lista, espera-se deletar o elemento
	 * 3.
	 */
	@Test
	public void deleteAfterTwoElementsTest() {
		list.add(1);
		list.add(2);
		list.add(3);
		list.deleteAfter(2);
	}

	/**
	 * Tenta deletar um elemento que tem sua próxima referencia como null.
	 */
	@Test
	public void deleteAfterNullReferenceTest() {
		list.add(1);
		list.add(2);
		list.add(null);
		list.deleteAfter(1);
	}

	/**
	 * Tenta deletar após um elemento que não está na lista.
	 */
	@Test
	public void deleteAfterNoElementTest() {
		list.deleteAfter(0);
	}

	/**
	 * Testa o método traverse em uma lista com 2 elementos.
	 */
	@Test
	public void traverseTest() {
		list.add(1);
		list.add(2);
		list.traverse();
	}

	/**
	 * Testa o método traverse em uma lista vazia.
	 */
	@Test
	public void traverseEmptyTest() {
		list.traverse();
	}

}
