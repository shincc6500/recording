from abc import ABCMeta, abstractmethod
from user.domain.user  import User

class IUserRepository(metaclass=ABCMeta):
    """
    CRUD 기능
    C : save
    R : find_by_email & username & id , get_user
    U : update, admin_update,
    D : delete, deactivate
    """
    # Create
    @abstractmethod
    def save(self, user: User):
        """
        Save a User entity.

        Parameters
        ----------
        self : object
           호출한 인스턴스 자신
        user : User
            저장할 User 도메인 객체

        Raises
        ------
        NotImplementedError
            하위 클래스에서 반드시 구현해야 함
        """
        raise NotImplementedError
    
    # Read
    @abstractmethod
    def find_by_email(self, email: str) -> User:
        """
        이메일로 유저를 검색 
        Parameters
        ----------
        self : object
           호출한 인스턴스 자신
        email : str
            검색에 사용할 유저의 이메일 주소
        Returns
        --------
        User : object
           조회된 유저 도메인 모델 객체

        Raises
        ------
        NotImplementedError
            하위 클래스에서 반드시 구현해야 함
        """
        raise NotImplementedError
    
    @abstractmethod
    def find_by_username(self, username: str) -> User:
        """
        로그인 아이디로 유저를 검색 
        Parameters
        ----------
        self : object
           호출한 인스턴스 자신
        username : str
            검색에 사용할 유저의 로그인 아이디
        Returns
        --------
        User : object
           조회된 유저 도메인 모델 객체

        Raises
        ------
        NotImplementedError
            하위 클래스에서 반드시 구현해야 함
        """
        raise NotImplementedError
    
    @abstractmethod
    def find_by_id(self, id: str) -> User:
        """
        id로 유저를 검색 
        Parameters
        ----------
        self : object
           호출한 인스턴스 자신
        id : str
            검색에 사용할 유저의 id ULID
        Returns
        --------
        User : object
           조회된 유저 도메인 모델 객체

        Raises
        ------
        NotImplementedError
            하위 클래스에서 반드시 구현해야 함
        """
        raise NotImplementedError
    
    @abstractmethod
    def get_users(self, page: int, items_per_page: int) -> tuple[int, list[User]]:
        '''
        유저 리스트를 페이징하여 출력
        Parameters
        ----------
        self : object
           호출한 인스턴스 자신
        page : int
            조회할 페이지 번호
        items_per_page : int
            페이지당 표시할 유저 수

        Returns
        --------
        tuple[int, list[User]]
            (전체 유저 수 또는 총 페이지 수, 조회된 유저 객체 리스트) 형태의 튜플
        
        '''
        raise NotImplementedError
    
    # Update
    @abstractmethod
    def update(self, user: User):
        """
        유저 정보 업데이트
        Parameters
        ----------
        self : object
           호출한 인스턴스 자신
        user : User
            수정할 유저 객체
        
        Raises
        ------
        NotImplementedError
            하위 클래스에서 반드시 구현해야 함
        """
        raise NotImplementedError
    
    @abstractmethod
    def admin_update(self, user: User):
        """
        관리자 개입 기반 유저 정보 업데이트
        Parameters
        ----------
        self : object
           호출한 인스턴스 자신
        user : User
            수정할 유저 객체
        
        Raises
        ------
        NotImplementedError
            하위 클래스에서 반드시 구현해야 함
        """
        raise NotImplementedError   
    
    @abstractmethod
    def delete(self, id: str):
        '''
        DB에서 유저 객체를 완전히 삭제(하드 삭제)
        Parameters
        ----------
        self: object
            호출한 인스턴스 자신
        id : str
            삭제할 user 객체의 id 값
        ---------
        raise
        NotImplementedError
            하위 클래스에서 반드시 구현해야 함
        '''
        raise NotImplementedError
    
    @abstractmethod
    def deactivate(self, id: str):
        '''
        DB에서 유저 객체를 비활성화(소프트 삭제)
        Parameters
        ----------
        self: object
            호출한 인스턴스 자신
        id : str
            비활성화할 user 객체의 id 값
        ---------
        raise
        NotImplementedError
            하위 클래스에서 반드시 구현해야 함
        '''
        raise NotImplementedError