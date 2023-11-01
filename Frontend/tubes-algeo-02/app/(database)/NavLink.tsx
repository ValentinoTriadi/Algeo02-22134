interface NavLink {
  route: string,
  link: string,
}

const NavbarLinks: NavLink[] = [
  {
    route: 'Dashboard',
    link: '/',
  },
  {
    route: 'CBIR',
    link: '/CBIR'
  },
  {
    route: 'Camera',
    link: '/camera',
  }
]