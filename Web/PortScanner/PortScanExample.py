import PortScanner as ps


def main():
    # Initialize a Scanner object that will scan top 50 commonly used ports.
    scanner = ps.PortScanner(target_ports=50)

    host_name = '127.0.0.1'

    scanner.set_thread_limit(1500)
    scanner.set_delay(15)
    scanner.show_target_ports()
    scanner.show_delay()
    scanner.show_top_k_ports(100)
    output = scanner.scan(host_name, message)
    
if __name__ == "__main__":
    main()
