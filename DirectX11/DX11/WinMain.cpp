#include "Windows.h"

/*

Refer�ncia

	LRESULT: Um tipo de dado definido pelo Windows para representar o resultado de uma mensagem de procedimento de janela.

	HWND: Um tipo de dado que representa um identificador de janela no Windows. 

	UINT: Um tipo de dado que representa n�meros inteiros n�o negativos.
	"msg" � o par�metro que representa o tipo de mensagem que est� sendo recebida, como WM_KEYDOWN, WM_MOUSEMOVE, WM_PAINT, etc.

	WPARAM: um tipo de dado que representa um par�metro relacionado ao tipo de mensagem. 
	"wparam" � o par�metro que cont�m informa��es adicionais sobre a mensagem, como tecla pressionada, bot�o do mouse pressionado, etc.

	LPARAM: um tipo de dado que representa um par�metro relacionado ao tipo de mensagem.
	"lparam" � o par�metro que cont�m informa��es adicionais sobre a mensagem, como coordenadas do mouse, dados adicionais, etc.

*/


LRESULT CALLBACK WndProc(HWND hwnd, UINT msg, WPARAM wparam, LPARAM lparam) {

	// In�cio do switch para lidar com diferentes tipos de mensagens
	switch (msg) {

		// Caso a mensagem seja WM_CLOSE (fechar a janela)
	case WM_CLOSE:
		// Envia uma mensagem para a fila de mensagens indicando o encerramento do aplicativo com o c�digo 69
		PostQuitMessage(69);
		// Sai do switch para evitar a chamada de DefWindowProc
		break;

	}

	// Se a mensagem n�o for WM_CLOSE ou n�o for tratada, chama a fun��o padr�o de procedimento de janela do sistema
	return DefWindowProc(hwnd, msg, wparam, lparam);

}

/*
Refer�ncia:

	CALLBACK: Uma macro definida no Windows que especifica a conven��o de chamada da fun��o. 
	No contexto do Windows, CALLBACK geralmente se traduz em __stdcall, que � uma conven��o de chamada de fun��o espec�fica do Windows.

	//

	_In_: Um modificador de anota��o usado para indicar que o argumento seguinte (HINSTANCE hInstance) � um par�metro de entrada. 
	N�o tem um efeito pr�tico no c�digo, mas pode ser usado por ferramentas de an�lise est�tica para entender o prop�sito do par�metro.

	_In_opt_: Modificador de anota��o usado para indicar que o argumento seguinte (HINSTANCE hPrevInstance) � um par�metro de entrada opcional.
	Neste caso, hPrevInstance representa uma inst�ncia anterior, mas � obsoleto e geralmente � NULL nos aplicativos modernos.

	//

	HINSTANCE: Tipo de dado que representa o identificador da inst�ncia do aplicativo. 
	Cada inst�ncia de um aplicativo Windows possui um identificador exclusivo.

	hInstance: Nome do primeiro par�metro, que � o identificador da inst�ncia do aplicativo. 
	Este identificador � passado pelo sistema operacional para que o aplicativo saiba qual inst�ncia est� sendo executada.

	hPrevInstance: Nome do segundo par�metro, que � obsoleto e geralmente � NULL. 
	Originalmente, era usado para identificar uma inst�ncia anterior do aplicativo, mas n�o � mais necess�rio.

	//

	LPSTR: Tipo de dado que representa um ponteiro para uma string de caracteres (C-string).

	lpCmdLine: Nome do terceiro par�metro, que � um ponteiro para uma string contendo os argumentos de linha de comando passados para o programa.
	Esses argumentos podem ser utilizados para configurar o comportamento do aplicativo.

	//

	nCmdShow: Nome do quarto par�metro, que especifica como a janela do aplicativo deve ser mostrada inicialmente.
	Pode ser um dos valores definidos nas constantes SW_ (por exemplo, SW_SHOWNORMAL, SW_HIDE, etc.).

*/

int CALLBACK WinMain( _In_ HINSTANCE hInstance, _In_opt_ HINSTANCE hPrevInstance, _In_ LPSTR lpCmdLina, _In_ int nCmdShow) {

	// Define o nome da classe da janela
	const auto pClassName = L"WindowClass";

	// Inicializa uma estrutura para configurar a classe de janela
	WNDCLASSEX wc = { 0 };
	wc.cbSize = sizeof(wc);            // Tamanho da estrutura
	wc.style = CS_OWNDC;                // Estilo da classe de janela (CS_OWNDC: cada janela tem seu pr�prio contexto de dispositivo gr�fico)
	wc.lpfnWndProc = DefWindowProc;     // Ponteiro para a fun��o de procedimento de janela padr�o
	wc.cbClsExtra = 0;                  // N�mero de bytes de espa�o extra alocados para a classe
	wc.cbWndExtra = 0;                  // N�mero de bytes de espa�o extra alocados para cada inst�ncia da janela
	wc.hInstance = hInstance;           // Inst�ncia do aplicativo associada � classe
	wc.hIcon = nullptr;                 // �cone associado � classe (nenhum neste caso)
	wc.hCursor = nullptr;               // Cursor associado � classe (nenhum neste caso)
	wc.hbrBackground = nullptr;         // Pincel de fundo usado para preencher a �rea de fundo da janela (nenhum neste caso)
	wc.lpszMenuName = nullptr;          // Nome do menu associado � classe (nenhum neste caso)
	wc.lpszClassName = pClassName;      // Nome da classe associado � estrutura

	// Registra a classe de janela usando a estrutura configurada
	RegisterClassEx(&wc);

	/*
	Refer�ncia:

		HWND: � um tipo de dado que representa um identificador de janela (Window Handle).
		HWND � frequentemente usado para se referir a janelas no ambiente Windows.
		
		//

		CreateWindowEx: Fun��o do Windows API usada para criar uma janela estendida.
		Ela permite a cria��o de uma janela com caracter�sticas espec�ficas.

		WS_CAPTION | WS_MINIMIZEBOX | WS_SYSMENU: O quarto par�metro s�o os estilos da janela. 
		Aqui, est�o sendo usados tr�s estilos combinados atrav�s do operador de bit a bit OR (|):

			WS_CAPTION: Adiciona uma barra de t�tulo � janela.
			WS_MINIMIZEBOX: Adiciona um bot�o de minimizar � barra de t�tulo.
			WS_SYSMENU: Adiciona um menu de sistema (menu ao clicar no �cone da janela).
	
	*/

	// Cria��o de uma janela utilizando a fun��o CreateWindowEx da Windows API.

	// Defini��o do identificador da janela (Handle to Window)
	HWND hwnd = CreateWindowEx(
		0,                       // Estilo estendido da janela (nenhum estilo estendido neste caso)
		pClassName,              // Nome da classe da janela, previamente registrado
		L"Window",               // T�tulo da janela (wstring indicado pelo prefixo "L")
		WS_CAPTION |             // Estilos da janela (barra de t�tulo)
		WS_MINIMIZEBOX |         // Estilos da janela (bot�o de minimizar)
		WS_SYSMENU,              // Estilos da janela (menu de sistema)
		200, 200,                 // Coordenadas iniciais da janela (x, y)
		640, 480,                 // Largura e altura da janela
		nullptr,                 // Identificador da janela pai (nenhum neste caso)
		nullptr,                 // Identificador de menu associado � janela (nenhum neste caso)
		hInstance,               // Identificador da inst�ncia do aplicativo associada � janela
		nullptr                  // Ponteiro para dados adicionais (nenhum neste caso)
	);

	// Fun��o ShowWindow utilizada para exibir a janela.
	ShowWindow(
		hwnd,      // Identificador da janela
		SW_SHOW    // Constante que especifica como a janela deve ser mostrada (neste caso, exibi��o normal)
	);


	MSG msg; // Declara uma vari�vel 'msg' do tipo MSG, que � usada para armazenar mensagens do Windows.
	BOOL gResult; // Declara uma vari�vel 'gResult' do tipo BOOL para armazenar o resultado da fun��o GetMessage.

	// Inicia um loop que continua at� que uma mensagem WM_QUIT seja recebida.
	while ( (gResult = GetMessage(&msg, nullptr, 0, 0)) > 0) {
		// A fun��o GetMessage obt�m uma mensagem da fila de mensagens.

		TranslateMessage(&msg); // Traduz mensagens de entrada
		DispatchMessage(&msg); // Despacha a mensagem para o procedimento da janela

	}

	// Ap�s o t�rmino do loop, verifica-se o resultado da execu��o do loop.
	if (gResult == -1) {

		// Se o valor retornado por GetMessage for -1, indica que houve um erro.
		return -1; // Retorna um c�digo de erro.

	}
	else {

		// Se o loop terminou normalmente, retorna o par�metro 'wParam' da �ltima mensagem.
		// O par�metro wParam � frequente usado para armazenar valores inteiros ou c�digos relacionados a uma mensagem.
		return msg.wParam;

	}

}