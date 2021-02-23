from inspect import getsourcefile
from os.path import abspath
import random

token = "7db3a1e3820df267ef560d7aeb6854b6713af45dc4e81baa34426711b5bdf9b2564b747861715bd27402f" # Место для токена сообщества
path = abspath(getsourcefile(lambda:0)).replace('\\', '/').replace('data.py','') # Определение пути к папке
print('\n\033[32m\033[40mТокен сообщества: \033[33m\033[40m' + str(token[0:8]) + '-...-' + str(token[len(token)-8:len(token)]))
print('\033[32m\033[40mТекущий путь к папке: \033[33m\033[40m' + path + '\033[37m\033[40m')

marketing_adm = []
student_adm = []

class Folder: # Папка в каталоге
    def __init__(self, name, text = None):
        self.name = name
        self.text = text

class Jpg: # Картинка в каталоге. Примечание: при создании объекта, путь обязательно должен содержать название файла вместе с его расширением
    def __init__(self, name, path):
        self.name = name
        self.path = path

class Pdf: # Документы в каталоге. Примечание: при создании объекта, путь обязательно должен содержать название файла вместе с его расширением
    def __init__(self, name, text, path, file_name):
        self.name = name
        self.text = text
        self.path = path
        self.file_name = file_name

class Media: # Медиа (картинка + надпись над ней). Примечание: при создании объекта, путь обязательно должен содержать название файла вместе с его расширением
    def __init__(self, name, text, path):
        self.name = name
        self.text = text
        self.path = path

def rand_el(array): # Возвращает рандомный элемент из массива
    return array[random.randint(0,len(array)-1)]

# Инициализация медиафайлов для каталога
m_0 = Media("[15.03.04] Автоматизация технологических процессов и производств",
'''1̲5̲.̲0̲3̲.̲0̲4̲ ̲А̲в̲т̲о̲м̲а̲т̲и̲з̲а̲ц̲и̲я̲ ̲т̲е̲х̲н̲о̲л̲о̲г̲и̲ч̲е̲с̲к̲и̲х̲ ̲п̲р̲о̲ц̲е̲с̲с̲о̲в̲ ̲и̲ ̲п̲р̲о̲и̲з̲в̲о̲д̲с̲т̲в̲
Выпускники, освоившие программу обретут навыки построения автоматизированных систем, освоят принципы функционирования и программирования средств автоматизации промышленных контроллеров.
Поступление на факультет: https://vsuet.ru/obuchenie/faculties/uits/specialty''', "Screens/150304.jpg")

m_1 = Media("[06.05.01] Биоинженерия и биоинформатика",
'''0̲6̲.̲0̲5̲.̲0̲1̲ ̲Б̲и̲о̲и̲н̲ж̲е̲н̲е̲р̲и̲я̲ ̲и̲ ̲б̲и̲о̲и̲н̲ф̲о̲р̲м̲а̲т̲и̲к̲а̲
Выпускники, освоившие программу обретут навыки, позволяющие получать и применять различные биологические объекты (от вирусов и одноклеточных до многоклеточных организмов), разрабатывать методы молекулярной диагностики и выбора новых мишеней для лекарственных препаратов, использовать методы генной инженерии для корректировки свойств биологических объектов, а знания в биоинформатике позволяют разрабатывать новые формы лекарственных систем.
Поступление на факультет: https://vsuet.ru/obuchenie/faculties/teh/specialty''', "Screens/60501.jpg")

m_2 = Media("[19.03.01] Биотехнология",
'''1̲9̲.̲0̲3̲.̲0̲1̲ ̲Б̲и̲о̲т̲е̲х̲н̲о̲л̲о̲г̲и̲я̲
Выпускники, освоившие программу обретут навыки, позволяющие выполнять проектные работы, направленные на разработку оптимальных условий биосинтеза целевых продуктов с заданными свойствами (кислоты, антибиотики, ферментные препараты) и участвовать в реализации биотехнологических процессов на производстве, в том числе с использованием технологии замкнутого цикла.
Поступление на факультет: https://vsuet.ru/obuchenie/faculties/teh/specialty''', "Screens/190301.jpg")

m_3 = Media("[36.03.01] Ветеринарно-санитарная экспертиза",
'''3̲6̲.̲0̲3̲.̲0̲1̲ ̲В̲е̲т̲е̲р̲и̲н̲а̲р̲н̲о̲-̲с̲а̲н̲и̲т̲а̲р̲н̲а̲я̲ ̲э̲к̲с̲п̲е̲р̲т̲и̲з̲а̲
Выпускники, освоившие программу обретут навыки по организации, планированию и осуществлению ветеринарно-санитарных мероприятий при экспорте/импорте продуктов питания, лабораторного анализа и экспертизы продукции пищевого назначения и разработки плановых и профилактических мероприятий, направленных на повышение безопасности в пищевой промышленности, а также изучат стандарты и нормативы в области ветеринарно-санитарного контроля.
Поступление на факультет: https://vsuet.ru/obuchenie/faculties/teh/specialty''', "Screens/360301.jpg")

m_4 = Media("[35.03.08] Водные биоресурсы и аквакультура",
'''3̲5̲.̲0̲3̲.̲0̲8̲ ̲В̲о̲д̲н̲ы̲е̲ ̲б̲и̲о̲р̲е̲с̲у̲р̲с̲ы̲ ̲и̲ ̲а̲к̲в̲а̲к̲у̲л̲ь̲т̲у̲р̲а̲
Выпускники, освоившие программу обретут навыки рационального использования и охраны биологических ресурсов, обеспечения экологической безопасности рыбохозяйственных водоемов, гидробионтов, процессов, объектов и продукции аквакультуры, а также проведения рыбохозяйственной экспертизы.
Поступление на факультет: https://vsuet.ru/obuchenie/faculties/uits/specialty''', "Screens/350308.jpg")

m_5 = Media("[43.03.03] Гостиничное дело",
'''4̲3̲.̲0̲3̲.̲0̲3̲ ̲Г̲о̲с̲т̲и̲н̲и̲ч̲н̲о̲е̲ ̲д̲е̲л̲о̲
Профессиональная деятельность бакалавров направлена на выполнение функций руководителя в любых средствах размещения от небольших гостиниц с домашней обстановкой до крупных гостиничных комплексов с развитой инфраструктурой. В ведении бакалавра находится вопрос организации обслуживания гостей в гостиницах и туристских комплексах. Он принимает, размещает, выписывает постояльцев, отвечает за бесперебойную работу объекта.
Трудоустройство в зависимости от квалификации (примеры компаний и организаций): VoronezhMarriottHotel, RamadaPlazaVoronezhCityCentre, СРК «Согдиана», ГК «Кудеяров стан», «PEGAS TOURISTIK», Воронежский визовый центр
https://vsuet.ru/obuchenie/faculties/eiu/specialty''', "Screens/430303.jpg")

m_6 = Media("[10.05.03] Информационная безопасность автоматизированных систем",
'''1̲0̲.̲0̲5̲.̲0̲3̲ ̲И̲н̲ф̲о̲р̲м̲а̲ц̲и̲о̲н̲н̲а̲я̲ ̲б̲е̲з̲о̲п̲а̲с̲н̲о̲с̲т̲ь̲ ̲а̲в̲т̲о̲м̲а̲т̲и̲з̲и̲р̲о̲в̲а̲н̲н̲ы̲х̲ ̲с̲и̲с̲т̲е̲м̲
Выпускники, освоившие программу обретут навыки работы с вычислительными центрами, техническими средствами, организации комплексной защиты, методами и средствами контроля информационной безопасности их создания и программирования.
Поступление на факультет: https://vsuet.ru/obuchenie/faculties/uits/specialty''', "Screens/100503.jpg")

m_7 = Media("[09.03.02] Информационные системы и технологии",
'''0̲9̲.̲0̲3̲.̲0̲2̲ ̲И̲н̲ф̲о̲р̲м̲а̲ц̲и̲о̲н̲н̲ы̲е̲ ̲с̲и̲с̲т̲е̲м̲ы̲ ̲и̲ ̲т̲е̲х̲н̲о̲л̲о̲г̲и̲и̲
Выпускники, освоившие программу обретут навыки разработки программного обеспечения компьютерных сетей, будут способны выполнять весь комплекс работ по установке, настройке и сопровождению программ, разрабатывать проекты автоматизированных систем работы вычислительных комплексов.
Поступление на факультет: https://vsuet.ru/obuchenie/faculties/uits/specialty''', "Screens/90302.jpg")

m_8 = Media("[38.03.02] Менеджмент",
'''3̲8̲.̲0̲3̲.̲0̲2̲ ̲М̲е̲н̲е̲д̲ж̲м̲е̲н̲т̲
Профессиональная деятельность бакалавра по направлению Менеджмент связана с участием в разработке и реализации корпоративной и конкурентной стратегии организации; планированием деятельности организации и подразделений; разработкой и реализацией проектов, направленных на развитие организации (предприятия, органа государственного или муниципального управления); мотивированием и стимулированием персонала организации, направленных на достижение стратегических и оперативных целей; оценкой эффективности проектов и управленческих решений; разработкой и реализацией бизнес-планов создания нового бизнеса.
В рамках реализации программы, у обучающихся формируются знания, умения и навыки, обеспечивающие способность эффективно выполнять функции, связанные с организацией товародвижения, оперативного управления транспортно-складскими процессами, анализа, планирования, подготовки решений по управлению запасами, закупками, логистической поддержки производственных и сбытовых операций.
Трудоустройство в зависимости от квалификации: Группа компаний «АГРОЭКО», СПАО «Ингострах»; ПАО «Сбербанк»; АО «Мукомольный комбинат «Воронежский»; ГК «ЭФКО», Союз «ТПП в Воронежской области», ФБУ «Воронежский ЦСМ», АО «Пятью пять», ПАО «Центрторг», АО «Тандер».
https://vsuet.ru/obuchenie/faculties/eiu/specialty''', "Screens/380302.jpg")

m_9 = Media("[09.03.03] Прикладная информатика",
'''0̲9̲.̲0̲3̲.̲0̲3̲ ̲П̲р̲и̲к̲л̲а̲д̲н̲а̲я̲ ̲и̲н̲ф̲о̲р̲м̲а̲т̲и̲к̲а̲
Выпускники, освоившие программу обретут навыки программирования и совершенствования прикладных и информационных процессов, операционных сред, информационных систем и средств коммуникации.
Поступление на факультет: https://vsuet.ru/obuchenie/faculties/uits/specialty''', "Screens/90303.jpg")

m_10 = Media("[15.03.03] Прикладная механика",
'''1̲5̲.̲0̲3̲.̲0̲3̲ ̲П̲р̲и̲к̲л̲а̲д̲н̲а̲я̲ ̲м̲е̲х̲а̲н̲и̲к̲а̲
Выпускники, освоившие программу обретут навыки проектирования и расчета машин и конструкций в строительстве, автомобильной, железнодорожной и авиационной промышленности с целью обеспечения прочности, устойчивости, надежности и износостойкости узлов и деталей с использованием программных систем компьютерного моделирования.
https://vsuet.ru/obuchenie/faculties/pma/specialty''', "Screens/150303.jpg")

m_11 = Media("[19.03.03] Продукты питания животного происхождения",
'''1̲9̲.̲0̲3̲.̲0̲3̲ ̲П̲р̲о̲д̲у̲к̲т̲ы̲ ̲п̲и̲т̲а̲н̲и̲я̲ ̲ж̲и̲в̲о̲т̲н̲о̲г̲о̲ ̲п̲р̲о̲и̲с̲х̲о̲ж̲д̲е̲н̲и̲я̲
Выпускники, освоившие программу обретут навыки, позволяющие участвовать в организации и проведении технологических процессов, проведении входного контроля качества сырья и материалов, производственного контроля полуфабрикатов, в разработке новых видов продукции и технологий в соответствии с государственной политикой РФ в области здорового питания.
Поступление на факультет: https://vsuet.ru/obuchenie/faculties/teh/specialty''', "Screens/190303.jpg")

m_12 = Media("[19.03.02] Продукты питания из растительного сырья",
'''1̲9̲.̲0̲3̲.̲0̲2̲ ̲П̲р̲о̲д̲у̲к̲т̲ы̲ ̲п̲и̲т̲а̲н̲и̲я̲ ̲и̲з̲ ̲р̲а̲с̲т̲и̲т̲е̲л̲ь̲н̲о̲г̲о̲ ̲с̲ы̲р̲ь̲я̲
Выпускники, освоившие программу обретут навыки по ведению производственными процессами и технологиями пищевых производств, в том числе в области биотехнологии; выполнения инженерно-проектных изысканий по усовершенствованию существующих и разработке новых технологических линий, организации контроля качества сырья и готовой продукции, и разработке рецептур продукции с учетом принципов энерго- и ресурсосбережения, а также получают знания в области стандартов и нормативов обеспечения безопасности пищевой продукции.
Поступление на факультет: https://vsuet.ru/obuchenie/faculties/teh/specialty''', "Screens/190302.jpg")

m_13 = Media("[15.05.01] Проектирование технологических машин и комплексов",
'''1̲5̲.̲0̲5̲.̲0̲1̲ ̲П̲р̲о̲е̲к̲т̲и̲р̲о̲в̲а̲н̲и̲е̲ ̲т̲е̲х̲н̲о̲л̲о̲г̲и̲ч̲е̲с̲к̲и̲х̲ ̲м̲а̲ш̲и̲н̲ ̲и̲ ̲к̲о̲м̲п̲л̲е̲к̲с̲о̲в̲
Выпускники, освоившие программу, обретут навыки выполнения проектно-конструкторских и научно-исследовательских работ с использованием современных компьютерных CAD/CAM/CAE-, PDM- и PLM- систем, разработки и внедрения в производство новых машин, оборудования и автоматизированных технологических комплексов, осуществления конструкторско-технологической подготовки производства.
https://vsuet.ru/obuchenie/faculties/pma/specialty''', "Screens/150501.jpg")

m_14 = Media("[43.03.01] Сервис",
'''4̲3̲.̲0̲3̲.̲0̲1̲ ̲С̲е̲р̲в̲и̲с̲
Выпускники, освоившие программу обретут навыки программирования, работы с базами данных, моделировании геоинформационных систем, средствами администрирования вычислительных систем,  геодезии и картографии, выполнения цифровой обработки картографических материалов, создания приложений для работы с геоданными.
Поступление на факультет: https://vsuet.ru/obuchenie/faculties/uits/specialty''', "Screens/430301.jpg")

m_15 = Media("[27.03.01] Стандартизация и метрология",
'''2̲7̲.̲0̲3̲.̲0̲1̲ ̲С̲т̲а̲н̲д̲а̲р̲т̲и̲з̲а̲ц̲и̲я̲ ̲и̲ ̲м̲е̲т̲р̲о̲л̲о̲г̲и̲я̲
Выпускники, освоившие программу обретут навыки по совершенствованию метрологического обеспечения и стандартов, правил, норм, использования современных методов контроля, измерений, испытаний, эксплуатации контрольно-измерительных средств.
Поступление на факультет: https://vsuet.ru/obuchenie/faculties/uits/specialty''', "Screens/270301.jpg")

m_16 = Media("[13.03.01] Теплоэнергетика и теплотехника",
'''1̲3̲.̲0̲3̲.̲0̲1̲ ̲Т̲е̲п̲л̲о̲э̲н̲е̲р̲г̲е̲т̲и̲к̲а̲ ̲и̲ ̲т̲е̲п̲л̲о̲т̲е̲х̲н̲и̲к̲а̲
Выпускники, освоившие программу обретут навыки разработки элементов конструкций и систем объектов  промышленной теплоэнергетики с использованием информационных технологий, выполнения монтажно-наладочных работ, эксплуатационного и сервисного обслуживания оборудования на предприятиях топливно-энергетического комплекса, атомных, тепловых и электростанциях.
https://vsuet.ru/obuchenie/faculties/pma/specialty''', "Screens/130301.jpg")

m_17 = Media("[15.03.02] Технологические машины и оборудование",
'''1̲5̲.̲0̲3̲.̲0̲2̲ ̲Т̲е̲х̲н̲о̲л̲о̲г̲и̲ч̲е̲с̲к̲и̲е̲ ̲м̲а̲ш̲и̲н̲ы̲ ̲и̲ ̲о̲б̲о̲р̲у̲д̲о̲в̲а̲н̲и̲е̲
Выпускники, освоившие программу, обретут навыки руководства работой коллективов исполнителей, осуществления контроля технологических процессов, монтажа, наладки, эксплуатации, обслуживания, настройки и проверки технического состояния оборудования, подготовки технической документации.
https://vsuet.ru/obuchenie/faculties/pma/specialty''', "Screens/150302.jpg")

m_18 = Media("[16.03.03] Технологические машины и оборудование",
'''1̲6̲.̲0̲3̲.̲0̲3̲ ̲Т̲е̲х̲н̲о̲л̲о̲г̲и̲ч̲е̲с̲к̲и̲е̲ ̲м̲а̲ш̲и̲н̲ы̲ ̲и̲ ̲о̲б̲о̲р̲у̲д̲о̲в̲а̲н̲и̲е̲
Выпускники, освоившие программу, обретут навыки проектирования систем холодильного и криогенного оборудования, проведения монтажных работ, технического обслуживания, диагностики и ремонта компрессорных холодильных установок, систем охлаждения, климатических установок и систем кондиционирования.
https://vsuet.ru/obuchenie/faculties/pma/specialty''', "Screens/160303.jpg")

m_19 = Media("[19.03.04] Технология продукции и организация общественного питания",
'''1̲9̲.̲0̲3̲.̲0̲4̲ ̲Т̲е̲х̲н̲о̲л̲о̲г̲и̲я̲ ̲п̲р̲о̲д̲у̲к̲ц̲и̲и̲ ̲и̲ ̲о̲р̲г̲а̲н̲и̲з̲а̲ц̲и̲я̲ ̲о̲б̲щ̲е̲с̲т̲в̲е̲н̲н̲о̲г̲о̲ ̲п̲и̲т̲а̲н̲и̲я̲
Профессиональная деятельность бакалавра связана с крупными сетевыми предприятиями питания и отелями, крупными специализированными цехами, имеющими функции кулинарного производства, центральными офисами сетей предприятий питания.
Трудоустройство в зависимости от квалификации (примеры компаний и организаций): ООО «Грабли», ООО «Нордис», ООО «Какие люди»
https://vsuet.ru/obuchenie/faculties/eiu/specialty''', "Screens/190304.jpg")

m_20 = Media("[20.03.01] Техносферная безопасность",
'''2̲0̲.̲0̲3̲.̲0̲1̲ ̲Т̲е̲х̲н̲о̲с̲ф̲е̲р̲н̲а̲я̲ ̲б̲е̲з̲о̲п̲а̲с̲н̲о̲с̲т̲ь̲
Выпускники, освоившие программу, обретут навыки охраны труда и техники безопасности на производственных объектах, обеспечения взрыво- и пожаробезопасности, предотвращения и ликвидации ЧС, оказания первой доврачебной помощи и экологической безопасности.
Поступление на факультет: https://vsuet.ru/obuchenie/faculties/uits/specialty''', "Screens/200301.jpg")

m_21 = Media("[27.03.04] Управление в технических системах",
'''2̲7̲.̲0̲3̲.̲0̲4̲ ̲У̲п̲р̲а̲в̲л̲е̲н̲и̲е̲ ̲в̲ ̲т̲е̲х̲н̲и̲ч̲е̲с̲к̲и̲х̲ ̲с̲и̲с̲т̲е̲м̲а̲х̲
Выпускники, освоившие программу обретут навыки моделирования, проектирования, создания  и внедрения современных интегрированных интеллектуальных комплексов, систем и средств управления производством.
Поступление на факультет: https://vsuet.ru/obuchenie/faculties/uits/specialty''', "Screens/270304.jpg")

m_22 = Media("[27.03.02] Управление качеством",
'''2̲7̲.̲0̲3̲.̲0̲2̲ ̲ ̲У̲п̲р̲а̲в̲л̲е̲н̲и̲е̲ ̲к̲а̲ч̲е̲с̲т̲в̲о̲м̲
Выпускники, освоившие программу обретут навыки сопровождению эффективной работы систем управления качеством, проведения мероприятий по улучшению качества продукции и оказания услуг, разработки методов и средств повышения безопасности и экологичности технологических процессов и внедрению информационных технологий в управление качеством.
Поступление на факультет: https://vsuet.ru/obuchenie/faculties/uits/specialty''', "Screens/270302.jpg")

m_23 = Media("[04.05.01] Фундаментальная и прикладная химия",
'''0̲4̲.̲0̲5̲.̲0̲1̲ ̲Ф̲у̲н̲д̲а̲м̲е̲н̲т̲а̲л̲ь̲н̲а̲я̲ ̲и̲ ̲п̲р̲и̲к̲л̲а̲д̲н̲а̲я̲ ̲х̲и̲м̲и̲я̲
Выпускники, освоившие программу, обретут навыки проведения экспертизы объектов окружающей среды, криминалистики, наркоконтроля, МЧС, медицинской диагностики и преподавания химии в образовательных организациях.
Поступление на факультет: https://vsuet.ru/obuchenie/faculties/uits/specialty''', "Screens/40501.jpg")

m_24 = Media("[18.03.01] Химическая технология",
'''1̲8̲.̲0̲3̲.̲0̲1̲ ̲Х̲и̲м̲и̲ч̲е̲с̲к̲а̲я̲ ̲т̲е̲х̲н̲о̲л̲о̲г̲и̲я̲
Выпускники, освоившие программу, обретут навыки создания, технологического сопровождения и участия в работах по  эксплуатации промышленных производств основных неорганических веществ, строительных материалов, продуктов основного и тонкого органического синтеза, полимерных материалов, продуктов переработки нефти, газа и твердого топлива, лекарственных препаратов и косметических средств.
Поступление на факультет: https://vsuet.ru/obuchenie/faculties/uits/specialty''', "Screens/180301.jpg")

m_25 = Media("[18.05.01] Химическая технология материалов современной энергетики",
'''1̲8̲.̲0̲5̲.̲0̲1̲ ̲Х̲и̲м̲и̲ч̲е̲с̲к̲а̲я̲ ̲т̲е̲х̲н̲о̲л̲о̲г̲и̲я̲ ̲м̲а̲т̲е̲р̲и̲а̲л̲о̲в̲ ̲с̲о̲в̲р̲е̲м̲е̲н̲н̲о̲й̲ ̲э̲н̲е̲р̲г̲е̲т̲и̲к̲и̲
Выпускники, освоившие программу, обретут навыки разработки процессов извлечения материалов ядерно-топливного цикла атомной энергетики из природного и техногенного сырья и мероприятий по защите окружающей среды от воздействия радиации.
Поступление на факультет: https://vsuet.ru/obuchenie/faculties/uits/specialty''', "Screens/180501.jpg")

m_26 = Media("[38.03.01] Экономика",
'''3̲8̲.̲0̲3̲.̲0̲1̲ ̲Э̲к̲о̲н̲о̲м̲и̲к̲а̲
Профессиональная деятельность бакалавра по направлению Экономика связана с экономическими, финансовыми, аналитическими службами организаций различных отраслей, сфер и форм собственности; с финансовыми, кредитными и страховыми учреждениями; с экономическими подразделениями органов государственной и муниципальной власти.
Трудоустройство в зависимости от квалификации (примеры компаний и организаций): ПАО «Сбербанк», АО ВНИИ Вега, Управление муниципальных закупок администрации городского округа город Воронеж, ПАО Молочный Комбинат «Воронежский», Федеральная налоговая служба.
https://vsuet.ru/obuchenie/faculties/eiu/specialty''', "Screens/380301.jpg")

m_27 = Media("[38.05.01] Экономическая безопасность",
'''3̲8̲.̲0̲5̲.̲0̲1̲ ̲Э̲к̲о̲н̲о̲м̲и̲ч̲е̲с̲к̲а̲я̲ ̲б̲е̲з̲о̲п̲а̲с̲н̲о̲с̲т̲ь̲
Профессиональная деятельность специалиста по экономической безопасности связана с проведением налоговых и аудиторских проверок, оценкой эффективности расходов, обеспечением законности и правопорядка в сфере экономики, планирование и проведение финансового контроля, предотвращением коррупционных преступлений в организациях различных отраслей, сфер и форм собственности.
Трудоустройство в зависимости от квалификации (примеры компаний и организаций): Управление муниципальных закупок администрации городского округа г. Воронеж, Международная аудиторская компания KPMG, Федеральная налоговая служба, Управление экономической безопасности и противодействия коррупции ГУ МВД РФ по Воронежской области, АО «Газпромбанк», АО «Россельхозбанк», ГК «ЭФКО».
https://vsuet.ru/obuchenie/faculties/eiu/specialty''', "Screens/380501.jpg")

m_28 = Media("[18.03.02] Энерго- и ресурсосберегающие процессы в химической технологии, нефтехимии и биотехнологии",
'''1̲8̲.̲0̲3̲.̲0̲2̲ ̲Э̲н̲е̲р̲г̲о̲-̲ ̲и̲ ̲р̲е̲с̲у̲р̲с̲о̲с̲б̲е̲р̲е̲г̲а̲ю̲щ̲и̲е̲ ̲п̲р̲о̲ц̲е̲с̲с̲ы̲ ̲
в̲ ̲х̲и̲м̲и̲ч̲е̲с̲к̲о̲й̲ ̲т̲е̲х̲н̲о̲л̲о̲г̲и̲и̲,̲ ̲н̲е̲ф̲т̲е̲х̲и̲м̲и̲и̲ ̲и̲ ̲б̲и̲о̲т̲е̲х̲н̲о̲л̲о̲г̲и̲и̲
Выпускники, освоившие программу, обретут навыки проектирования и эксплуатации оборудования химических и нефтехимических производств и систем искусственного интеллекта в химической технологии, нефтехимии и биотехнологии, навыки  оценки состояния окружающей среды и защиты ее от антропогенного воздействия.
Поступление на факультет: https://vsuet.ru/obuchenie/faculties/uits/specialty''', "Screens/180302.jpg")

# Инициализация документов для каталога
p_0 = Pdf("Как подать документы❓", "Подробная инструкция:", "Documents(.pdf)/300.pdf", "Инструкция по подаче документов")
p_1 = Pdf("Даты", "Расписание экзаменов и сроки приема:", "Documents(.pdf)/400.pdf", "Даты и сроки приема документов")

# Инициализация картинок для каталога
j_0 = Jpg("Котик", "Pictures(.jpg)/cat_0.jpg")
j_1 = Jpg("Котик", "Pictures(.jpg)/cat_1.jpg")
j_2 = Jpg("Котик", "Pictures(.jpg)/cat_2.jpg")
j_3 = Jpg("Котик", "Pictures(.jpg)/cat_3.jpg")
j_4 = Jpg("Котик", "Pictures(.jpg)/cat_4.jpg")
j_5 = Jpg("Котик", "Pictures(.jpg)/cat_5.jpg")
j_6 = Jpg("Котик", "Pictures(.jpg)/cat_6.jpg")
j_7 = Jpg("Котик", "Pictures(.jpg)/cat_7.jpg")
j_8 = Jpg("Котик", "Pictures(.jpg)/cat_8.jpg")

# Дополнительно
cats = [j_0, j_1, j_2, j_3, j_4, j_5, j_6, j_7, j_8]
misund = ['Что ты имел ввиду?', 'Не понял, повтори:', 'Пожалуйста, не перепутай:', 'Выбери нужный вариант:', 'Было бы лучше, если бы ты выбрал один из вариатов:', 'Не понял, о чем ты?!',
          '-❓❔❓❔❓-', '⬇ Выбери один из вариантов ответов ⬇']
first_decoration = ['Да, слушаю 🙂', 'Чем могу помочь? 😃', 'Выбирай:', 'Ну что там еще?', 'Что рассказать?', 'Какой вопрос тебя интересует?']
second_decoration = ['О чем ты хочешь узнать больше?', 'Вот что я могу рассказать', 'Поясню:', 'Чем ты увлекаешься?', 'Что из этого тебя интересует?']
notification = ['Администрация скоро рассмотрит твой вопрос 😌', 'Не переживай, тебе скоро ответят 🙂', 'Помощник 🤖: Интересно.. Уверен, тебе скоро ответят']
answers = {}
answers[frozenset({'справку', 'заказать'})] = 'Для этого есть деканат - закажи справку там, позвонив по телефону, который можешь найти на нашем сайте: https://vsuet.ru/sveden/struct'
answers[frozenset({'справку', 'достать'})] = 'Для этого есть деканат - закажи справку там, позвонив по телефону, который можешь найти на нашем сайте: https://vsuet.ru/sveden/struct'
answers[frozenset({'справку', 'взять'})] = 'Для этого есть деканат - закажи справку там, позвонив по телефону, который можешь найти на нашем сайте: https://vsuet.ru/sveden/struct'
answers[frozenset({'факультеты', 'университете'})] = 'В университете 6 выпускающих факультетов – управления и информатики в технологических системах; экологии и химической технологии; технологический; пищевых машин и автоматов; экономики и управления, среднего профессионального образования. Помимо них, в вузе функционируют факультет безотрывного образования, международный факультет, факультет довузовской подготовки, факультет гуманитарного образования и воспитания.'
answers[frozenset({'расписание'})] = 'Расписание занятий доступно по ссылке: https://vsuet.ru/student/schedule'
answers[frozenset({'формы', 'обучения'})] = '''В вузе реализуются образовательные программы следующих уровней:
среднее профессиональное образование;
высшее образование – бакалавриат;
высшее образование – специалитет;
высшее образование –  магистратура;
высшее образование – подготовка научно-педагогических кадров в аспирантуре.
Формы обучения
В университете реализуются очная, заочная и очно-заочная формы обучения.'''
answers[frozenset({'рейтинг', 'студентов'})] = "Рейтинг успеваемости студентов доступен по ссылке: http://rating.vsuet.ru/web/Ved/Default.aspx"
answers[frozenset({'рейтинг', 'мой'})] = "Рейтинг успеваемости студентов доступен по ссылке: http://rating.vsuet.ru/web/Ved/Default.aspx"
answers[frozenset({'каникулы'})] = "У студентов всех форм предусмотрены зимние и летние каникулы."
answers[frozenset({'за', 'отчислить'})] = "Обучающегося могут отчислить из университета из-за неуспеваемости или задержки платы за обучение, за неуважительные пропуски занятий. Это сложный процесс для обучающегося и для образовательной организации. Причины такого решения разнообразны. Каждый конкретный случай требует индивидуального рассмотрения."
answers[frozenset({'почему', 'отчислить'})] = "Обучающегося могут отчислить из университета из-за неуспеваемости или задержки платы за обучение, за неуважительные пропуски занятий. Это сложный процесс для обучающегося и для образовательной организации. Причины такого решения разнообразны. Каждый конкретный случай требует индивидуального рассмотрения."
answers[frozenset({'почему', 'отчислили'})] = "Обучающегося могут отчислить из университета из-за неуспеваемости или задержки платы за обучение, за неуважительные пропуски занятий. Это сложный процесс для обучающегося и для образовательной организации. Причины такого решения разнообразны. Каждый конкретный случай требует индивидуального рассмотрения."
answers[frozenset({'без', 'ЕГЭ'})] = 'В вуз можно поступить по внутренним испытаниям на базе диплома выпускника СПО.'
answers[frozenset({'перевод', 'из'})] = 'Да, возможен. Информация о переводе доступна по ссылке: https://vsuet.ru/sveden/vacant'
answers[frozenset({'как', 'студенческий'})] = 'Документы вручаются на первой встрече обучающихся с куратором групп.'
answers[frozenset({'как', 'зачетную'})] = 'Документы вручаются на первой встрече обучающихся с куратором групп.'
answers[frozenset({'как', 'пропуск'})] = 'Документы вручаются на первой встрече обучающихся с куратором групп.'
answers[frozenset({'где', 'студенческий'})] = 'Документы вручаются на первой встрече обучающихся с куратором групп.'
answers[frozenset({'где', 'зачетную'})] = 'Документы вручаются на первой встрече обучающихся с куратором групп.'
answers[frozenset({'где', 'пропуск'})] = 'Документы вручаются на первой встрече обучающихся с куратором групп.'
answers[frozenset({'утерял'})] = 'При утере одного из документов необходимо обратиться в деканат.'
answers[frozenset({'утерян'})] = 'При утере одного из документов необходимо обратиться в деканат.'
answers[frozenset({'потерял'})] = 'При утере одного из документов необходимо обратиться в деканат.'
answers[frozenset({'потерян'})] = 'При утере одного из документов необходимо обратиться в деканат.'
answers[frozenset({'стипендия'})] = 'Возможно, ответ можно найти по ссылке: https://vsuet.ru/chavo/grants'
answers[frozenset({'стипендии'})] = 'Возможно, ответ можно найти по ссылке: https://vsuet.ru/chavo/grants'

# Инициализация папок для каталога
f_0 = Folder("Кем стать❓", "Выбери свое профессиональное направление:\n")
f_1 = Folder("Какие ЕГЭ сдавать❓", "Один предмет. Какой?\n")
f_2 = Folder("Подробнее о направлениях подготовки", "Какое направление подготовки тебя интерисует?\n")
f_3 = Folder("Как подать документы❓")
f_4 = Folder("Мне нужны даты❗")
f_5 = Folder("IT-шником", rand_el(second_decoration))
f_6 = Folder("Технологом", rand_el(second_decoration))
f_7 = Folder("Экологом", rand_el(second_decoration))
f_8 = Folder("Специалистом по производственной безопасности",rand_el(second_decoration))
f_9 = Folder("Экономистом", rand_el(second_decoration))
f_10 = Folder("Управленцем", rand_el(second_decoration))
f_11 = Folder("Проектировщиком", rand_el(second_decoration))
f_12 = Folder("Инженером-Механиком", rand_el(second_decoration))
f_13 = Folder("Биоинженером", rand_el(second_decoration))
f_14 = Folder("Ветеринарным экспертом", rand_el(second_decoration))
f_15 = Folder("Физика", rand_el(second_decoration))
f_16 = Folder("Информатика", rand_el(second_decoration))
f_17 = Folder("Химия", rand_el(second_decoration))
f_18 = Folder("Обществознание", rand_el(second_decoration))
f_19 = Folder("Биология", rand_el(second_decoration))

# План каталога
MAIN_ARCHIVE = {
f_0:{
  f_5:{m_6, m_7, m_9, m_21, m_14, m_0},
  f_6:{m_23, m_24, m_25, m_28, m_2, m_11, m_12, m_19, m_15, m_22},
  f_7:{m_28, m_25},
  f_8:{m_20},
  f_9:{m_26, m_27},
  f_10:{m_8, m_5},
  f_11:{m_16, m_10, m_13, m_28},
  f_12:{m_28, m_10, m_18, m_17},
  f_13:{m_4, m_1},
  f_14:{m_3, m_1}
  },
f_1:{
  f_15:{m_7, m_16, m_10, m_0, m_13, m_15, m_22, m_21},
  f_16:{m_9, m_6},
  f_17:{m_23, m_24, m_28, m_25, m_2, m_12, m_11, m_19, m_20},
  f_18:{m_1, m_4, m_3},
  f_19:{m_26, m_8, m_27, m_14, m_5},
  },
f_2:{m_0, m_1, m_2, m_3, m_4, m_5, m_6, m_7, m_8, m_9, m_10, m_11, m_12, m_13, m_14, m_15, m_16, m_17, m_18, m_19, m_20, m_21, m_22, m_23, m_24, m_25, m_26, m_27, m_28},
p_0:{},
p_1:{}
}
