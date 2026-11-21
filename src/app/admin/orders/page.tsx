'use client';

import React, { useState, useMemo } from 'react';
import Link from 'next/link';
import {
  useReactTable,
  getCoreRowModel,
  getFilteredRowModel,
  getPaginationRowModel,
  getSortedRowModel,
  createColumnHelper,
  flexRender,
} from '@tanstack/react-table';
import { useLanguage } from '@/context/LanguageContext';
import { formatPrice } from '@/lib/utils';
import {
  Search,
  CheckCircle2,
  Clock,
  Truck,
  XCircle,
  Eye,
  ArrowUpDown,
  Filter,
  Download,
} from 'lucide-react';

interface AdminOrder {
  id: string;
  orderNumber: string;
  customerName: string;
  phone: string;
  governorate: string;
  itemsSummary: string;
  total: number;
  paymentMethod: string;
  status: 'PENDING' | 'PROCESSING' | 'SHIPPED' | 'DELIVERED' | 'CANCELLED';
  date: string;
}

const mockOrders: AdminOrder[] = [
  {
    id: 'ord-1',
    orderNumber: 'MESS-842910',
    customerName: 'م. أحمد الشناوي (شركة النيل)',
    phone: '01012345678',
    governorate: 'القاهرة (التجمع)',
    itemsSummary: 'Cisco C1000-24P + 2x UniFi U6',
    total: 35678,
    paymentMethod: 'COD',
    status: 'SHIPPED',
    date: '2026-11-21 14:30',
  },
  {
    id: 'ord-2',
    orderNumber: 'MESS-842911',
    customerName: 'د. كريم فهمي',
    phone: '01198765432',
    governorate: 'الجيزة (الدقي)',
    itemsSummary: 'Synology DS923+ 4-Bay NAS',
    total: 27940,
    paymentMethod: 'COD',
    status: 'PROCESSING',
    date: '2026-11-21 15:10',
  },
  {
    id: 'ord-3',
    orderNumber: 'MESS-842912',
    customerName: 'محمود عبد العزيز',
    phone: '01234567890',
    governorate: 'الإسكندرية (سموحة)',
    itemsSummary: 'APC Smart-UPS 1500VA',
    total: 18480,
    paymentMethod: 'COD',
    status: 'PENDING',
    date: '2026-11-21 16:05',
  },
  {
    id: 'ord-4',
    orderNumber: 'MESS-842908',
    customerName: 'م. حسام الدين حسن',
    phone: '01055554433',
    governorate: 'الدقهلية (المنصورة)',
    itemsSummary: 'D-Link Cat6 Cable 305m (2x)',
    total: 6900,
    paymentMethod: 'COD',
    status: 'DELIVERED',
    date: '2026-11-20 11:20',
  },
  {
    id: 'ord-5',
    orderNumber: 'MESS-842907',
    customerName: 'طارق صلاح',
    phone: '01511223344',
    governorate: 'القليوبية (بنها)',
    itemsSummary: 'Grandstream GRP2615 IP Phone',
    total: 4289,
    paymentMethod: 'COD',
    status: 'DELIVERED',
    date: '2026-11-20 09:45',
  },
];

const columnHelper = createColumnHelper<AdminOrder>();

export default function AdminOrdersPage() {
  const { locale, t } = useLanguage();
  const [data, setData] = useState<AdminOrder[]>(mockOrders);
  const [globalFilter, setGlobalFilter] = useState('');
  const [statusFilter, setStatusFilter] = useState<string>('ALL');

  const updateOrderStatus = (orderId: string, newStatus: AdminOrder['status']) => {
    setData((prev) =>
      prev.map((order) => (order.id === orderId ? { ...order, status: newStatus } : order))
    );
  };

  const filteredData = useMemo(() => {
    return data.filter((item) => {
      if (statusFilter !== 'ALL' && item.status !== statusFilter) return false;
      if (!globalFilter) return true;
      const q = globalFilter.toLowerCase();
      return (
        item.orderNumber.toLowerCase().includes(q) ||
        item.customerName.toLowerCase().includes(q) ||
        item.phone.includes(q) ||
        item.governorate.toLowerCase().includes(q)
      );
    });
  }, [data, statusFilter, globalFilter]);

  const columns = useMemo(
    () => [
      columnHelper.accessor('orderNumber', {
        header: 'رقم الطلب',
        cell: (info) => (
          <span className="font-mono font-bold text-petrol-700 bg-petrol-50 px-2.5 py-1 rounded-md border border-petrol-100">
            {info.getValue()}
          </span>
        ),
      }),
      columnHelper.accessor('customerName', {
        header: 'العميل والتفاصيل',
        cell: (info) => (
          <div>
            <span className="font-bold text-petrol-900 block leading-snug">{info.getValue()}</span>
            <span className="text-[11px] font-mono text-slate-400">{info.row.original.phone}</span>
          </div>
        ),
      }),
      columnHelper.accessor('governorate', {
        header: 'المحافظة',
        cell: (info) => <span className="text-slate-700 font-medium">{info.getValue()}</span>,
      }),
      columnHelper.accessor('itemsSummary', {
        header: 'المنتجات المطلوبة',
        cell: (info) => (
          <span className="text-xs text-slate-600 line-clamp-1 max-w-[200px]" title={info.getValue()}>
            {info.getValue()}
          </span>
        ),
      }),
      columnHelper.accessor('total', {
        header: 'الإجمالي (ج.م)',
        cell: (info) => (
          <span className="font-mono font-black text-petrol-950">
            {formatPrice(info.getValue(), locale)}
          </span>
        ),
      }),
      columnHelper.accessor('status', {
        header: 'الحالة وتغييرها',
        cell: (info) => {
          const val = info.getValue();
          const colorMap = {
            PENDING: 'bg-amber-50 text-amber-700 border-amber-200',
            PROCESSING: 'bg-indigo-50 text-indigo-700 border-indigo-200',
            SHIPPED: 'bg-sky-50 text-sky-700 border-sky-200',
            DELIVERED: 'bg-emerald-50 text-emerald-700 border-emerald-200',
            CANCELLED: 'bg-rose-50 text-rose-700 border-rose-200',
          };

          return (
            <select
              value={val}
              onChange={(e) =>
                updateOrderStatus(info.row.original.id, e.target.value as AdminOrder['status'])
              }
              className={`text-xs font-bold rounded-lg px-2.5 py-1 border focus:outline-none ${colorMap[val]}`}
            >
              <option value="PENDING">جديد (قيد المراجعة)</option>
              <option value="PROCESSING">قيد التجهيز بالمستودع</option>
              <option value="SHIPPED">خرج مع المندوب</option>
              <option value="DELIVERED">تم التسليم بنجاح</option>
              <option value="CANCELLED">ملغي</option>
            </select>
          );
        },
      }),
    ],
    [locale]
  );

  const table = useReactTable({
    data: filteredData,
    columns,
    getCoreRowModel: getCoreRowModel(),
    getSortedRowModel: getSortedRowModel(),
    getPaginationRowModel: getPaginationRowModel(),
  });

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10 space-y-6">
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-slate-200 pb-4">
        <div>
          <span className="text-xs font-mono font-bold text-sky-600 bg-sky-50 px-2 py-0.5 rounded">
            POWERED BY TANSTACK TABLE v8
          </span>
          <h1 className="text-2xl font-black text-petrol-900 mt-1">{t('adminOrders')}</h1>
          <p className="text-xs text-slate-500">إدارة وجدولة طلبات التوريد والشحن لعملاء مصر (COD)</p>
        </div>

        <button
          onClick={() => alert('تم تصدير شيت الطلبات بصيغة CSV')}
          className="inline-flex items-center gap-2 px-4 py-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-800 text-xs font-bold transition-colors"
        >
          <Download className="w-4 h-4" />
          <span>تصدير الطلبات CSV</span>
        </button>
      </div>

      {/* Filter and Search Bar */}
      <div className="bg-white p-4 rounded-2xl border border-slate-200 shadow-subtle flex flex-col sm:flex-row items-center justify-between gap-4">
        {/* Search */}
        <div className="relative w-full sm:w-80">
          <Search className="w-4 h-4 text-slate-400 absolute top-1/2 -translate-y-1/2 start-3" />
          <input
            type="text"
            value={globalFilter}
            onChange={(e) => setGlobalFilter(e.target.value)}
            placeholder="بحث برقم الطلب، اسم العميل، الهاتف..."
            className="w-full ps-9 pe-4 py-2 text-xs rounded-xl border border-slate-200 focus:outline-none focus:ring-2 focus:ring-petrol-500"
          />
        </div>

        {/* Status Filters */}
        <div className="flex items-center gap-1.5 overflow-x-auto w-full sm:w-auto text-xs font-bold">
          {['ALL', 'PENDING', 'PROCESSING', 'SHIPPED', 'DELIVERED'].map((st) => (
            <button
              key={st}
              onClick={() => setStatusFilter(st)}
              className={`px-3 py-1.5 rounded-lg whitespace-nowrap transition-colors ${
                statusFilter === st
                  ? 'bg-petrol-700 text-white'
                  : 'bg-slate-100 text-slate-600 hover:bg-slate-200'
              }`}
            >
              {st === 'ALL'
                ? 'الكل'
                : st === 'PENDING'
                ? 'جديد'
                : st === 'PROCESSING'
                ? 'قيد التجهيز'
                : st === 'SHIPPED'
                ? 'خرج للشحن'
                : 'مكتمل'}
            </button>
          ))}
        </div>
      </div>

      {/* TanStack Data Table */}
      <div className="bg-white rounded-2xl border border-slate-200 shadow-subtle overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full text-xs">
            <thead>
              {table.getHeaderGroups().map((headerGroup) => (
                <tr key={headerGroup.id} className="bg-slate-50 border-b border-slate-200">
                  {headerGroup.headers.map((header) => (
                    <th key={header.id} className="p-3.5 text-start font-bold text-slate-600">
                      {flexRender(header.column.columnDef.header, header.getContext())}
                    </th>
                  ))}
                </tr>
              ))}
            </thead>
            <tbody className="divide-y divide-slate-100">
              {table.getRowModel().rows.map((row) => (
                <tr key={row.id} className="hover:bg-slate-50/70 transition-colors">
                  {row.getVisibleCells().map((cell) => (
                    <td key={cell.id} className="p-3.5">
                      {flexRender(cell.column.columnDef.cell, cell.getContext())}
                    </td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
