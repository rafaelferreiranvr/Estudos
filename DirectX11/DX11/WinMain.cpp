#include "Windows.h"

/*

Referência

	LRESULT: Um tipo de dado definido pelo Windows para representar o resultado de uma mensagem de procedimento de janela.

	HWND: Um tipo de dado que representa um identificador de janela no Windows. 

	UINT: Um tipo de dado que representa números inteiros não negativos.
	"msg" é o parâmetro que representa o tipo de mensagem que está sendo recebida, como WM_KEYDOWN, WM_MOUSEMOVE, WM_PAINT, etc.

	WPARAM: um tipo de dado que representa um parâmetro relacionado ao tipo de mensagem. 
	"wparam" é o parâmetro que contém informações adicionais sobre a mensagem, como tecla pressionada, botão do mouse pressionado, etc.

	LPARAM: um tipo de dado que representa um parâmetro relacionado ao tipo de mensagem.
	"lparam" é o parâmetro que contém informações adicionais sobre a mensagem, como coordenadas do mouse, dados adicionais, etc.

*/


LRESULT CALLBACK WndProc(HWND hwnd, UINT msg, WPARAM wparam, LPARAM lparam) {

	// Início do switch para lidar com diferentes tipos de mensagens
	switch (msg) {

		// Caso a mensagem seja WM_CLOSE (fechar a janela)
	case WM_CLOSE:
		// Envia uma mensagem para a fila de mensagens indicando o encerramento do aplicativo com o código 69
		PostQuitMessage(69);
		// Sai do switch para evitar a chamada de DefWindowProc
		break;

	}

	// Se a mensagem não for WM_CLOSE ou não for tratada, chama a função padrão de procedimento de janela do sistema
	return DefWindowProc(hwnd, msg, wparam, lparam);

}

/*
Referência:

	CALLBACK: Uma macro definida no Windows que especifica a convenção de chamada da função. 
	No contexto do Windows, CALLBACK geralmente se traduz em __stdcall, que é uma convenção de chamada de função específica do Windows.

	//

	_In_: Um modificador de anotação usado para indicar que o argumento seguinte (HINSTANCE hInstance) é um parâmetro de entrada. 
	Não tem um efeito prático no código, mas pode ser usado por ferramentas de análise estática para entender o propósito do parâmetro.

	_In_opt_: Modificador de anotação usado para indicar que o argumento seguinte (HINSTANCE hPrevInstance) é um parâmetro de entrada opcional.
	Neste caso, hPrevInstance representa uma instância anterior, mas é obsoleto e geralmente é NULL nos aplicativos modernos.

	//

	HINSTANCE: Tipo de dado que representa o identificador da instância do aplicativo. 
	Cada instância de um aplicativo Windows possui um identificador exclusivo.

	hInstance: Nome do primeiro parâmetro, que é o identificador da instância do aplicativo. 
	Este identificador é passado pelo sistema operacional para que o aplicativo saiba qual instância está sendo executada.

	hPrevInstance: Nome do segundo parâmetro, que é obsoleto e geralmente é NULL. 
	Originalmente, era usado para identificar uma instância anterior do aplicativo, mas não é mais necessário.

	//

	LPSTR: Tipo de dado que representa um ponteiro para uma string de caracteres (C-string).

	lpCmdLine: Nome do terceiro parâmetro, que é um ponteiro para uma string contendo os argumentos de linha de comando passados para o programa.
	Esses argumentos podem ser utilizados para configurar o comportamento do aplicativo.

	//

	nCmdShow: Nome do quarto parâmetro, que especifica como a janela do aplicativo deve ser mostrada inicialmente.
	Pode ser um dos valores definidos nas constantes SW_ (por exemplo, SW_SHOWNORMAL, SW_HIDE, etc.).

*/

int CALLBACK WinMain( _In_ HINSTANCE hInstance, _In_opt_ HINSTANCE hPrevInstance, _In_ LPSTR lpCmdLina, _In_ int nCmdShow) {

	// Define o nome da classe da janela
	const auto pClassName = L"WindowClass";

	// Inicializa uma estrutura para configurar a classe de janela
	WNDCLASSEX wc = { 0 };
	wc.cbSize = sizeof(wc);            // Tamanho da estrutura
	wc.style = CS_OWNDC;                // Estilo da classe de janela (CS_OWNDC: cada janela tem seu próprio contexto de dispositivo gráfico)
	wc.lpfnWndProc = DefWindowProc;     // Ponteiro para a função de procedimento de janela padrão
	wc.cbClsExtra = 0;                  // Número de bytes de espaço extra alocados para a classe
	wc.cbWndExtra = 0;                  // Número de bytes de espaço extra alocados para cada instância da janela
	wc.hInstance = hInstance;           // Instância do aplicativo associada à classe
	wc.hIcon = nullptr;                 // Ícone associado à classe (nenhum neste caso)
	wc.hCursor = nullptr;               // Cursor associado à classe (nenhum neste caso)
	wc.hbrBackground = nullptr;         // Pincel de fundo usado para preencher a área de fundo da janela (nenhum neste caso)
	wc.lpszMenuName = nullptr;          // Nome do menu associado à classe (nenhum neste caso)
	wc.lpszClassName = pClassName;      // Nome da classe associado à estrutura

	// Registra a classe de janela usando a estrutura configurada
	RegisterClassEx(&wc);

	/*
	Referência:

		HWND: É um tipo de dado que representa um identificador de janela (Window Handle).
		HWND é frequentemente usado para se referir a janelas no ambiente Windows.
		
		//

		CreateWindowEx: Função do Windows API usada para criar uma janela estendida.
		Ela permite a criação de uma janela com características específicas.

		WS_CAPTION | WS_MINIMIZEBOX | WS_SYSMENU: O quarto parâmetro são os estilos da janela. 
		Aqui, estão sendo usados três estilos combinados através do operador de bit a bit OR (|):

			WS_CAPTION: Adiciona uma barra de título à janela.
			WS_MINIMIZEBOX: Adiciona um botão de minimizar à barra de título.
			WS_SYSMENU: Adiciona um menu de sistema (menu ao clicar no ícone da janela).
	
	*/

	// Criação de uma janela utilizando a função CreateWindowEx da Windows API.

	// Definição do identificador da janela (Handle to Window)
	HWND hwnd = CreateWindowEx(
		0,                       // Estilo estendido da janela (nenhum estilo estendido neste caso)
		pClassName,              // Nome da classe da janela, previamente registrado
		L"Window",               // Título da janela (wstring indicado pelo prefixo "L")
		WS_CAPTION |             // Estilos da janela (barra de título)
		WS_MINIMIZEBOX |         // Estilos da janela (botão de minimizar)
		WS_SYSMENU,              // Estilos da janela (menu de sistema)
		200, 200,                 // Coordenadas iniciais da janela (x, y)
		640, 480,                 // Largura e altura da janela
		nullptr,                 // Identificador da janela pai (nenhum neste caso)
		nullptr,                 // Identificador de menu associado à janela (nenhum neste caso)
		hInstance,               // Identificador da instância do aplicativo associada à janela
		nullptr                  // Ponteiro para dados adicionais (nenhum neste caso)
	);

	// Função ShowWindow utilizada para exibir a janela.
	ShowWindow(
		hwnd,      // Identificador da janela
		SW_SHOW    // Constante que especifica como a janela deve ser mostrada (neste caso, exibição normal)
	);


	MSG msg; // Declara uma variável 'msg' do tipo MSG, que é usada para armazenar mensagens do Windows.
	BOOL gResult; // Declara uma variável 'gResult' do tipo BOOL para armazenar o resultado da função GetMessage.

	// Inicia um loop que continua até que uma mensagem WM_QUIT seja recebida.
	while ( (gResult = GetMessage(&msg, nullptr, 0, 0)) > 0) {
		// A função GetMessage obtém uma mensagem da fila de mensagens.

		TranslateMessage(&msg); // Traduz mensagens de entrada
		DispatchMessage(&msg); // Despacha a mensagem para o procedimento da janela

	}

	// Após o término do loop, verifica-se o resultado da execução do loop.
	if (gResult == -1) {

		// Se o valor retornado por GetMessage for -1, indica que houve um erro.
		return -1; // Retorna um código de erro.

	}
	else {

		// Se o loop terminou normalmente, retorna o parâmetro 'wParam' da última mensagem.
		// O parâmetro wParam é frequente usado para armazenar valores inteiros ou códigos relacionados a uma mensagem.
		return msg.wParam;

	}

}